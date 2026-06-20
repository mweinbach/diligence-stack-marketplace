# Diligence Stack MCP playbook

## Corpus policy

| Key | Visibility | Use |
|---|---|---|
| `diligence-stack-reports` | Shared paid-subscriber knowledge base | Default source for Diligence Stack reports, market primers, vendor notes, charts, transcripts, and uploaded report material. |
| `equity-research` | Private, entitlement-dependent | Optional external analyst perspective. Use only when returned by `list_catalog`; label private-source conclusions and keep them out of redistributable artifacts. |

Catalog contents and dates change. Never hardcode corpus counts, publishers, tickers, categories, or coverage dates into an answer.

## Correct call sequence

1. `list_catalog` with no knowledge-base filter.
2. If filtering, `list_catalog` again using the canonical key and requested facet.
3. `search` using only returned keys and exact facet values.
4. `fetch` selected returned evidence IDs.
5. `get_document` only when broader context is needed.
6. Repeat search with a counter-thesis, risk, or falsification query.

## Search design

- Put concepts, mechanisms, entities, and the decision question in the semantic query.
- Put exact ticker, publisher, category, title, date, and evidence type in filters.
- Prefer `group_by_document: true` for discovery; turn it off only when multiple passages from the same document are specifically useful.
- Use `exclude_sections` to reduce disclosures, legal boilerplate, or other noise, but still inspect every result's `section`; classification can be imperfect.
- Treat `publication_date: null` as unknown. Fall back to source and indexed dates without relabeling them as publication dates.
- If `staleness_warning` is true, say so. If `filter_truncated` is true, narrow the filters and rerun.

## Retrieval design

- Fetch evidence IDs, not invented IDs or arbitrary URLs.
- Preserve the returned locator. A page number and a heading path are both valid locators.
- For a chart or image, request both `text` and `image`; use the derived text for accessibility and inspect the image when visual structure matters.
- For paginated reports, request the smallest inclusive page range that resolves context.
- For page-less Markdown packets, call `get_document` without `pages`. A page range on a page-less asset may return an empty result.
- Follow `next_cursor` rather than guessing subsequent pages or offsets.

## Citation record

For each material claim retain:

| Field | Requirement |
|---|---|
| Title and publisher | Always |
| Publication date | If present; otherwise label source/indexed date accurately |
| Locator | Page or heading path |
| Evidence ID | Always |
| Asset ID | When document context was retrieved |
| Knowledge base | Always; mark private equity research |
| URL | Link only to an HTTPS page whose exact host is `www.thediligencestack.com`; otherwise leave the citation unlinked |
| Claim type and confidence | Preserve when the evidence supplies them; otherwise assign and label as your assessment |

Render house-research citations as `The Diligence Stack — “{title},” {date}, {locator} (Evidence {id}).` Render separately entitled material as `Accessed via The Diligence Stack — {publisher}, “{title},” {date}, {locator} (private; Evidence {id}).` Preserve the original publisher without presenting its work as the Diligence Stack house view.

Never expose portal, MCP, authenticated-original, admin, Substack, publisher, vendor, data-room, or other third-party links. Never turn one of those URLs into a supposedly public citation. If no canonical Diligence Stack page exists, retain the title, date, locator, and evidence ID as unlinked text.
