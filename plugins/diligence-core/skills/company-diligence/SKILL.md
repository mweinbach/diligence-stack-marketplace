---
name: company-diligence
description: Build a source-linked company or vendor diligence packet using Diligence Stack reports, vendor notes, and optionally entitled equity research. Use for company briefs, competitive positioning, thesis updates, catalysts, risks, monitoring dashboards, or investment research.
---

# Company Diligence

Build a living thesis that connects technical or market mechanisms to business outcomes and observable proof.

## Research sequence

1. Follow the `diligence-research` catalog-first MCP workflow.
2. Resolve the exact ticker and relevant categories from `list_catalog`. Search the shared `diligence-stack-reports` corpus first.
3. Search separately for the company, competitors, market architecture, risks, disconfirming evidence, and dated watch items.
4. If `equity-research` is authorized, use it as a private comparative source - not as the house view. Search across multiple publishers and recent dates; separate substantive analysis from disclosures and valuation boilerplate.
5. Fetch the evidence behind material claims. Retrieve the full vendor packet or report sections when snippets omit mechanism, assumptions, or caveats.
6. Reconcile Diligence Stack analysis, company claims, and external analyst views. Do not average disagreement away.

## Analytical frame

For each thesis component show:

`driver -> mechanism -> business implication -> strategic read-through -> observable signal -> confidence`

Evaluate:

- market role and architecture control;
- product and workload fit;
- customer proof, concentration, and production conversion;
- revenue quality, pricing architecture, and unit economics;
- supply, delivery, and ecosystem dependencies;
- competitive response and substitution risk;
- optionality versus evidence already in the base case;
- catalysts, watch items, and explicit falsification conditions.

For enterprise AI companies, distinguish the model/runtime/interface layer, orchestration/workflow layer, and system-of-record/governance layer when relevant. Weight production conversion and sustained usage more heavily than pilots, benchmarks, or new-logo announcements.

## Output

Use [the company packet](references/company-packet.md). Label every metric as public fact, primary research, licensed research, derived estimate, or analyst judgment. Preserve ranges and confidence; do not manufacture false precision.
