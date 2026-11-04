# Limitations

## Current constraints (MVP + early polish)

### Model editing

- Read-only application: DEXPI Studio does not edit models

### Validation depth

- Validation is primarily schema + structural checks
- No configurable domain-rule packs in-app

### Scale and performance

- Very large models may still show slower tree/search population
- Rendering/search responsiveness depends on model size and diagram complexity

### Search UX boundaries

- Search currently focuses on tag/type/id patterns through `QueryEngine`
- Grouped/clustered result views are not implemented yet

### Export workflow

- Export UX is intentionally thin over pyDEXPI exporters
- No export preview pipeline in GUI yet

### General workflow

- Single model loaded at a time
- No project/session multi-file workspace yet
