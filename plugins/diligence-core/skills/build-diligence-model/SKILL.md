---
name: build-diligence-model
description: Build a source-linked, driver-based diligence model with assumptions, scenarios, sensitivities, checks, and evidence provenance. Use for market sizing, revenue builds, unit economics, capacity models, margin or EPS bridges, operating models, valuation inputs, or any spreadsheet/model request grounded in Diligence Stack research.
---

# Build Diligence Model

Turn a research thesis into a transparent model whose assumptions can be tested and updated.

## Brand contract

Before producing user-facing content, read and apply [the Diligence Stack brand guidelines](../diligence-brand-guidelines/SKILL.md). Use its color, typography, logo, citation, and link defaults unless the user explicitly requests different visual styling; its attribution and canonical-link rules always apply.

## Workflow

1. Define the decision, model output, forecast horizon, frequency, currency, units, and required precision.
2. Follow the `diligence-research` catalog -> search -> fetch -> document workflow. Use the subscriber corpus first and separately entitled equity research only when authorized.
3. Create a driver tree before entering values. Connect operating inputs to revenue, profit, cash flow, capacity, or market size rather than plugging headline outputs.
4. Separate historical facts, company guidance, third-party estimates, Diligence Stack derived estimates, and analyst assumptions.
5. Add an assumption register containing source date, locator, evidence ID, claim type, confidence, and update trigger for every material input.
6. Build base, upside, and downside cases from explicit driver changes. Avoid stacking multiple assumptions that express the same risk.
7. Add sensitivities around the two or three variables with the greatest decision impact.
8. Reconcile totals, units, growth rates, margins, cash flow, and scenario direction. Include zero, negative, delayed, and capacity-constrained cases where plausible.
9. State which outputs are model results rather than sourced facts and which new evidence would change them.

## Model construction

For a workbook, prefer separate sections or tabs for cover/readme, sources, historicals, assumptions, drivers, scenarios, outputs, sensitivities, and checks. Use formulas for calculated values; do not hardcode the same assumption in multiple places.

Read [the model blueprint](references/model-blueprint.md) before constructing a model. Use [the worked examples](references/model-examples.md) to select formulas, not as factual data. Use [the audit checklist](references/model-audit.md) before delivery.

If current primary data is required and is not in the MCP corpus, obtain it from an authorized current source or label the gap. Never invent historical financials, consensus, or management guidance.

## Output

Deliver the model or model specification plus:

- driver tree and formula map;
- assumption and evidence register;
- scenario definitions;
- sensitivity results;
- model checks and unresolved gaps;
- concise interpretation of what actually drives the conclusion.
