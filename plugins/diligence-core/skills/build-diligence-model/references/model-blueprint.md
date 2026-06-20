# Driver-model blueprint

## Recommended structure

| Section | Purpose |
|---|---|
| Cover / README | Scope, version, units, dates, scenario selected, and limitations |
| Sources | Evidence IDs, source labels, locators, dates, access class, and links |
| Historicals | Reported or verified observations only |
| Assumptions | One canonical location for forecast drivers |
| Drivers | Operational build by product, workload, customer, capacity, or cohort |
| Scenarios | Base/upside/downside changes by driver |
| Outputs | Market size, revenue, margin, cash flow, valuation input, or decision metric |
| Sensitivities | Two-way or one-way tables for high-impact variables |
| Checks | Balance, unit, sign, scenario, and reconciliation tests |

## Assumption register

| ID | Assumption | Value / range | Unit | Period | Scenario | Source class | Confidence | Evidence ID / locator | Update trigger |
|---|---|---:|---|---|---|---|---|---|---|

## Formula rules

- State units in every row and normalize before arithmetic.
- Put assumptions in one place and reference them.
- Keep sourced values distinct from formulas and judgments.
- Use ranges when evidence cannot support point precision.
- Separate volume, price, mix, utilization, attach, timing, and FX.
- Show constraints explicitly: supply, capacity, qualification, financing, or adoption.
- Include a model output only if its driver chain can be explained in one sentence.

## Scenario design

Scenarios should reflect coherent worlds, not arbitrary percentage changes. For each scenario state:

1. what changes operationally;
2. why it changes;
3. which evidence supports that possibility;
4. which observable signal selects the scenario;
5. whether the assumption is independent of other scenario changes.
