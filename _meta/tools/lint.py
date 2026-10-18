"""lint.py v0.2 — implements subject pack v0.2 §9 (L-01..L-16).
usage: python3 _meta/tools/lint.py <wiki root>   (reads wiki/, _meta/source-registry.csv, _meta/tools/terms.txt)"""
import re,os,sys,csv,collections
root=sys.argv[1]; wiki=os.path.join(root,'wiki')
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
rows=list(csv.DictReader(open(os.path.join(root,'_meta','source-registry.csv'))))
reg={r['src_id'] for r in rows}
pending=set()
for r in rows:
    if r['state']!='ingested':
        pending|={r['src_id'],os.path.splitext(os.path.basename(r['path']))[0]}
        pending|={x for x in r['legacy_ids'].split('|') if x}
# terms
sec=None; T=collections.defaultdict(list)
for l in open(os.path.join(root,'_meta','tools','terms.txt')):
    l=l.strip()
    if not l or l.startswith('#'): continue
    if l.startswith('['): sec=l[1:-1]; continue
    T[sec]+= [l] if sec=='compound' else l.split()
compounds=set(c.lower() for c in T['compound'])
for t in T['locked']:
    if '_' in t: compounds.add(t.replace('_',' ').lower())
ABBR=set(T['abbr']); CAMEL=set(T['camel'])
DOM='PPC|LST|CTLG|INV|VOC|OFF|ECON|HLTH|INTEL|CUST|LNCH|PRCE|AGCY|MEAS|WIKI'
GEN='REF|PROC|TECH|DATASPEC|MAP|META|TEMPL|DIAG|CASE|GLOSS|DEC|DECRULE'
IDRE=re.compile(rf'^({DOM})-({GEN})-\d{{3}}$')
CODES=set(DOM.split('|'))|set(GEN.split('|'))|{'IF','THEN','WARN','BLOCK','INFO'}  # pack-defined keywords: DECRULE section names, lint severities
REQ=['id','title','genre','domain','page_status','prov_tag','evidence_scope','sources','recorded','producer','page_version','schema_version']
REQ_GENRE={'DEC':['decision_date','date_source']}
BANNED=re.compile(r'\b(layer|tier|stage|level)s?\b',re.I)
ABRE=re.compile(r'(?<![\w-])([A-Z][A-Z0-9&+]{1,})(?![\w-])')
CAMRE=re.compile(r'\b[a-z]+[A-Z][A-Za-z]*\b')
slugs={f[:-3] for f in os.listdir(wiki) if f.endswith('.md')}
def padded(block):
    import pad; return pad.fmt(block)==block
def strip_code_links(s):
    s=re.sub(r'```.*?```','',s,flags=re.S)
    s=re.sub(r'`[^`]*`','',s)
    s=re.sub(r'\[\[[^\]]*\]\]','',s)
    return s
ids=collections.Counter(); out=[]; inbound=collections.Counter(); pages={}
for f in sorted(os.listdir(wiki)):
    if not f.endswith('.md'): continue
    t=open(os.path.join(wiki,f)).read(); L=t.split('\n'); pages[f]=t
    def R(rule,sev,msg): out.append((f,rule,sev,msg))
    if L[0]!='---' or '---' not in L[1:]: R('L-01','BLOCK','fence'); continue
    end=L[1:].index('---')+1; fm='\n'.join(L[1:end]); body='\n'.join(L[end+1:])
    keys={m.group(1):m.group(2).strip() for m in re.finditer(r'^([a-z_]+):\s*(.*)$',fm,re.M)}
    req=REQ+REQ_GENRE.get(keys.get('genre'),[])
    if 'Client' in keys.get('entity_types',''): req=req+['project_tier']
    for k in req:
        if k not in keys: R('L-02','BLOCK',f'missing {k}')
    pid=keys.get('id',''); ids[pid]+=1
    if not IDRE.match(pid): R('L-03','BLOCK',f'bad id {pid}')
    for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]',t):
        tgt,alias=m.group(1),m.group(2)
        if tgt in slugs: inbound[tgt]+= (tgt!=f[:-3])
        elif tgt in pending or (alias in pending): R('L-04a','INFO',f'pending [[{tgt}]]')
        else: R('L-04b','WARN',f'broken [[{tgt}]]')
    blinks=re.findall(r'\[\[([^\]|#]+)',body)
    for l,c in collections.Counter(blinks).items():
        if c>1: R('L-05','WARN',f'dup link {l} x{c}')
    claims=re.findall(r'`(prov:[^`]*)`',body); provs=[]
    for c in claims:
        fl={}
        for p in re.split(r'\s*(?<!\\)\|\s*|\s*\\\|\s*',c):
            if ':' in p: k,v=p.split(':',1); fl[k.strip()]=v.strip()
        for k in ('prov','scope','src'):
            if k not in fl: R('L-07','BLOCK',f'claim missing {k}: {c[:50]}')
        for s in fl.get('src','').split(','):
            if s.strip() and s.strip() not in reg: R('L-08','BLOCK',f'src {s} not in registry')
        if fl.get('prov')=='V' and 'verified_by' not in keys: R('L-06','BLOCK','V without verified_by')
        if keys.get('genre')=='DECRULE' and 'autonomy' not in fl: R('L-13','BLOCK','DECRULE claim no autonomy')
        provs.append(fl.get('prov'))
    if not claims: R('L-07','BLOCK','no claim lines')
    order='XUDV'
    if provs and keys.get('prov_tag')!=min(provs,key=lambda p:order.index(p) if p in order else 0): R('L-09','FIX','prov_tag != lowest claim prov')
    if keys.get('page_status')=='superseded' and 'superseded_by' not in keys: R('L-10','BLOCK','no superseded_by')
    plain=strip_code_links(body)
    for line in plain.split('\n'):
        low=line.lower()
        for m in BANNED.finditer(line):
            if not any(c in low and low.find(c)<=m.start()<low.find(c)+len(c) for c in compounds):
                R('L-11','WARN',f'bare word "{m.group(0)}"')
        for m in ABRE.finditer(line):
            tok=m.group(1)
            if tok not in ABBR and tok not in CODES and not re.fullmatch(r'[A-Z]+-?\d+',tok):
                R('L-11','WARN',f'abbr "{tok}"')
        for m in CAMRE.finditer(line):
            if m.group(0) not in CAMEL and m.group(0) not in ABBR: R('L-11','WARN',f'camelCase "{m.group(0)}"')
    if re.search(r'\bdriver',plain,re.I) and not re.search(r'causal:\s*(intervention|counterfactual)',body): R('L-14','WARN','"driver" without causal>=intervention')
    # L-16 tables padded
    import pad
    fence=False; i=0; BL=body.split('\n')
    while i<len(BL):
        if BL[i].lstrip().startswith('```'): fence=not fence; i+=1; continue
        if not fence and BL[i].lstrip().startswith('|'):
            j=i
            while j<len(BL) and BL[j].lstrip().startswith('|'): j+=1
            if pad.fmt(BL[i:j])!=BL[i:j]: R('L-16','WARN',f'unpadded table at body line {i+1}')
            i=j; continue
        i+=1
    out.append((f,'_stats','',f'claims={len(claims)}'))
# L-12 cross-page
import itertools
CL=[]
for f,t in pages.items():
    for c in re.findall(r'`(prov:[^`]*)`',t):
        fl={}
        for p in re.split(r'\s*(?<!\\)\|\s*|\s*\\\|\s*',c):
            if ':' in p: k,v=p.split(':',1); fl[k.strip()]=v.strip()
        CL.append((f,fl))
scopes=collections.defaultdict(set)
for f,fl in CL:
    for s in fl.get('src','').split(','): scopes[s.strip()].add(fl.get('scope'))
for f,fl in CL:
    if fl.get('scope')=='global':
        for s in fl.get('src','').split(','):
            if scopes[s.strip()]=={'entity_only'}: out.append((f,'L-12','WARN',f'global claim cites all-entity_only {s}'))
for i,c in ids.items():
    if c>1: out.append(('*','L-03','BLOCK',f'dup id {i}'))
for f in pages:
    if inbound[f[:-3]]==0: out.append((f,'L-15','WARN','no inbound link'))
for r in out: print('\t'.join(r))
