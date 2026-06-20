---
name: find-research-exhibits
description: Find and assemble source-linked charts, tables, scorecards, heat maps, architecture diagrams, and other exhibits from the Diligence Stack MCP. Use for exhibit books, memo or deck support, chart discovery, visual evidence, source verification, or locating the best existing graphic for a research question.
---

# Find Research Exhibits

Retrieve the strongest existing visual evidence without confusing a chart description with the chart itself.

## Workflow

1. Define the claim the exhibit must support, audience, format, and whether private sources are allowed.
2. Call `list_catalog` and discover current categories and evidence types. Search with `evidence_kinds: ["chart", "image"]` when appropriate.
3. Use `group_by_document: true` for discovery, then inspect additional matches for related exhibits in the same report.
4. Fetch selected evidence IDs with `include: ["text", "image", "original_link"]`.
5. Inspect both derived text and the image. Verify title, axes, units, period, legend, sample, source, methodology, and whether the graphic actually supports the intended claim.
6. Retrieve adjacent document pages for caption and narrative context.
7. Rank exhibits by decision relevance, source quality, readability, freshness, and redistribution rights.
8. Build an exhibit index and explain what each graphic proves, does not prove, and where it belongs.

Use [the exhibit index](references/exhibit-index.md).

## Boundaries

The MCP retrieves source material but does not render new charts. Use an authorized visualization or spreadsheet workflow if the user asks for a new graphic. Do not expose authenticated original links or private equity-research exhibits to viewers who may lack access.
