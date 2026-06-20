---
name: track-investment-thesis
description: Convert diligence research into a living thesis with evidence, key performance indicators, catalysts, risks, falsification conditions, review dates, and confidence changes. Use for thesis trackers, monitoring dashboards, watch lists, quarterly updates, portfolio reviews, or deciding whether new evidence changes a company or market view.
---

# Track Investment Thesis

Make the thesis observable and updateable rather than static prose.

## Workflow

1. State the current thesis, decision, time horizon, and confidence.
2. Break it into independent thesis components using `driver -> mechanism -> business implication`.
3. Follow `diligence-research` to retrieve supporting and contradicting evidence. Record the latest evidence date, not merely the report date.
4. For each component define a leading indicator, lagging confirmation, falsification condition, threshold, expected timing, and next review date.
5. Separate thesis evidence from valuation, sentiment, and price movement.
6. When updating, search only the period since the prior review plus any late-indexed documents. Compare new evidence with the prior state and log the delta.
7. Change confidence only when evidence crosses a stated threshold. Explain why unchanged news did not change the view.
8. Escalate stale evidence, broken assumptions, and signals that cannot be monitored.

Use [the tracker template](references/thesis-tracker.md). If a source-linked model exists, map each monitoring signal to the assumption or output it changes.

## Output

Return the current thesis, the changed evidence, confidence delta, triggered conditions, upcoming catalysts, and next research actions. Never call ordinary volatility a thesis break without linking it to the operating mechanism.
