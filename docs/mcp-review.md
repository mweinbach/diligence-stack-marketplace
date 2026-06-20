# Diligence Stack MCP review

Reviewed live on 2026-06-19 against the OAuth-authorized read-only server.

## What works well

- The four-tool surface is small and coherent: catalog, search, evidence fetch, and document retrieval.
- OAuth grants prune corpus access, allowing a shared paid-subscriber knowledge base and separately entitled private equity research on one endpoint.
- Search results preserve evidence and asset IDs, source metadata, locators, sections, freshness, duplicate status, match reasons, and additional passages.
- Evidence fetch can return derived text, authenticated images, and original-document links.
- Document retrieval supports inclusive page ranges and opaque continuation cursors.
- The corpus includes agent-ready vendor packets with explicit claim types, confidence, metrics, reasoning maps, definitions, and watch items.

## Recommended server improvements

### P0 — usability and correctness

1. Accept a knowledge-base display name as an alias or return the canonical key in the validation error. `DiligenceStack Reports` currently fails where `diligence-stack-reports` succeeds.
2. Return an explanatory validation error when `pages` is supplied for a page-less document. The current behavior can return an empty successful result; suggest retrying without `pages`.
3. Tighten section classification. Substantive searches with disclosure/legal exclusions can still surface valuation-method and risk boilerplate labeled `substantive`.
4. Add an explicit visibility field such as `access_class: shared | private` to each catalog entry so clients can explain corpus boundaries without inferring from names.

### P1 — discovery and ranking

1. Populate currently null counts for category, evidence-type, document-type, and date facets.
2. Align facet and filter vocabulary: the facet is `evidence_types`, while search accepts `evidence_kinds`; either alias both or document the mapping in tool output.
3. Either allow `document_types` as a search filter or stop advertising it as a facet that appears filter-like.
4. Improve ticker-filter ranking to favor current, company-specific substantive research over broad index reports, old reports, and disclosure sections.
5. Populate `evidenceCount` in catalog metadata or omit the field rather than returning null.

### P2 — context efficiency and citation UX

1. Avoid returning the same large payload in both text content and structured content when the client supports structured results.
2. Distinguish canonical public URLs, authenticated original links, and internal admin URLs in separate typed fields.
3. Add a concise citation object to fetched evidence with a ready-to-render label, date basis, and access requirement.
4. Expose a server/schema version in catalog metadata so marketplace skills can declare compatibility.

## Skill-side mitigations implemented

- Catalog-first calls and canonical-key use.
- Shared subscriber corpus by default; private equity research only after an explicit catalog grant.
- Search → fetch → document retrieval provenance chain.
- Separate behavior for paginated reports and page-less ingestion packets.
- Section, staleness, truncation, duplicate, date-basis, and URL-access checks.
- No private research content embedded in the plugin.
