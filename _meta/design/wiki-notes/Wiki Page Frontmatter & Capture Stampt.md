- **Wiki page frontmatter**, written by me. It carries 
	- id and aliases, 
	- genre, 
	- entity_types, 
	- domain, 
	- page_status, 
	- a computed prov_tag, 
	- evidence_scope, 
	- sources, 
	- valid_from/to + recorded,
	- verified_by/on, 
	- disclosure_level, 
	- classification, 
	- versions, and 
	- relationships.

- **Capture stamp** for when you save output from current LLM sessions. You fill 5 fields: 
	- `captured`, `source_type: llm-session`, `producer: llm`, `session_ref`, `contains_client_data`. I fill the rest at ingest.

Store a single `page_status` (seed / candidate / promoted / superseded)