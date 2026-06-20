---
name: equity-research-brief
description: Synthesize separately entitled private equity research alongside the Diligence Stack house view. Use for ticker briefs, consensus and disagreement maps, catalysts, earnings preparation, valuation debates, or analyst-view comparisons when the equity-research corpus is authorized.
---

# Equity Research Brief

Use private research carefully and make access boundaries visible.

## Brand contract

Before producing user-facing content, read and apply [the Diligence Stack brand guidelines](../diligence-brand-guidelines/SKILL.md). Use its color, typography, logo, citation, and link defaults unless the user explicitly requests different visual styling; its attribution and canonical-link rules always apply.

## Access gate

1. Call `list_catalog` with no filter.
2. Continue only if the canonical `equity-research` key is returned. If absent, say that private equity research is not available for this connection and offer a public-only brief from `diligence-stack-reports`.
3. Never embed private report text, examples, identifiers, publisher lists, or derived summaries in plugin source or generally shareable artifacts.

## Research workflow

1. Discover the exact ticker, publisher, and date facets. Do not guess issuer aliases.
2. Search by ticker with a substantive question and a recent date range. Use `exclude_sections` to reduce disclosure/legal noise, but verify each result's actual section.
3. Sample multiple publishers where coverage permits. Separate company material, independent research, and Diligence Stack house analysis.
4. Fetch only the evidence needed to support the comparison. Retrieve document context for estimates, valuation, methodology, and risk language.
5. Search for the bull case, bear case, estimate revisions, catalysts, valuation assumptions, and disconfirming evidence separately.
6. Treat price targets, ratings, and estimates as dated source views, never facts or personalized advice.

## Output

- Current debate and evidence window
- Diligence Stack house view
- External research consensus
- Material disagreements by mechanism and assumption
- Estimate and valuation ranges with dates and publishers
- Catalysts, risks, and falsification signals
- Gaps and stale evidence
- Private source ledger with title, publisher, date, locator, and evidence ID

Mark the output **Private - authorized research**. Paraphrase; do not reproduce substantial report text. Do not expose authenticated original-document links in an output intended for people who may lack access.
