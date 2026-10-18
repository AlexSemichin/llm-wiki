"""Pad markdown tables Obsidian-style: '| cell |', cells left-aligned and padded to column width,
delimiter dashes = column width (min 3). Splits on unescaped pipes only. Skips fenced code blocks.
Usage: pad.py in out   |   pad.py --check file  (exit 1 if any table unpadded)"""
import re, sys
SPLIT = re.compile(r'(?<!\\)\|')
def cells(line):
    s = line.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|') and not s.endswith('\\|'): s = s[:-1]
    return [c.strip() for c in SPLIT.split(s)]
def is_delim(cs): return all(re.fullmatch(r':?-{1,}:?', c) for c in cs)
def fmt(block):
    rows = [cells(l) for l in block]
    n = max(len(r) for r in rows)
    rows = [r + ['']*(n-len(r)) for r in rows]
    w = [max(3, max(len(r[i]) for j,r in enumerate(rows) if j != 1)) for i in range(n)]
    out = []
    for j, r in enumerate(rows):
        if j == 1:
            parts = []
            for i, c in enumerate(r):
                l, rr = c.startswith(':'), c.endswith(':') and len(c) > 1
                d = '-'*(w[i]-l-rr); parts.append((':' if l else '')+d+(':' if rr else ''))
        else:
            parts = [c.ljust(w[i]) for i, c in enumerate(r)]
        out.append('| ' + ' | '.join(parts) + ' |')
    return out
def process(text):
    lines = text.split('\n'); out = []; i = 0; fence = False
    while i < len(lines):
        l = lines[i]
        if l.lstrip().startswith('```'): fence = not fence; out.append(l); i += 1; continue
        if not fence and l.lstrip().startswith('|') and i+1 < len(lines) and lines[i+1].lstrip().startswith('|') and is_delim(cells(lines[i+1])):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith('|'): j += 1
            out += fmt(lines[i:j]); i = j; continue
        out.append(l); i += 1
    return '\n'.join(out)
if __name__ == '__main__':
    if sys.argv[1] == '--check':
        t = open(sys.argv[2]).read(); ok = process(t) == t
        print('L-16', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
    src = open(sys.argv[1]).read()  # read fully before opening the target (in-place safe)
    open(sys.argv[2], 'w').write(process(src))
