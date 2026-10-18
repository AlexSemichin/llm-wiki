**Stack 4 Artifacts**
* schema wiki layer is `CLAUDE.md` 
* plus the subject pack, 
* wiki layer is the page frontmatter, and 
* lint is a deterministic script.

| What I kept                                                                | Where it goes                                                                                  |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **V1–V5 verifier ranks + the tag-upgrade rule**                                | `CLAUDE.md` §Provenance, the `verified_by` / `verified_on` frontmatter fields, and a lint rule |
| **Client vs subject split (T2/T1) + the anonymized route for client evidence** | `CLAUDE.md` §Client data, the `contains_client_data` field on captures, and the CASE template  |
| **Semver**                                                                     | `page_version` / `schema_version` on every page, plus `schema` entries in log.md               |

Wiki pages may link to vault artifacts, but vault content doesn’t get compiled into wiki pages.