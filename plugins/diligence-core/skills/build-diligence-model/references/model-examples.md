# Synthetic modeling examples

These examples illustrate structure only. All values are fictional and must never be presented as Diligence Stack evidence.

## 1. Market-size model

```text
Addressable units = Installed base * Eligible share
Annual deployments = Addressable units * Annual adoption rate
Market revenue = Annual deployments * Content per deployment
```

Example:

| Driver | Base | Upside | Downside |
|---|---:|---:|---:|
| Installed sites | 1,000 | 1,000 | 1,000 |
| Eligible share | 60% | 70% | 45% |
| Annual adoption | 20% | 30% | 10% |
| Content per site | $2.0m | $2.3m | $1.6m |

Base market revenue = `1,000 * 60% * 20% * $2.0m = $240m`.

## 2. Capacity-constrained infrastructure model

```text
Monetizable capacity = Energized capacity * Utilization
Revenue = Monetizable capacity * Revenue per capacity unit
Gross profit = Revenue * Gross margin
```

Model announced, contracted, energized, and monetizable capacity separately. Backlog is not revenue and physical capacity is not automatically utilized capacity.

## 3. Product revenue build

```text
Product revenue = Units shipped * Average selling price
Service revenue = Installed base * Service attach * Service price
Total revenue = Product revenue + Service revenue
```

Separate qualification, order, shipment, deployment, and customer-acceptance timing when the cycle is long.

## 4. SaaS / workflow model

```text
Ending customers = Beginning customers + New customers - Churned customers
Subscription revenue = Average customers * Average contract value
AI revenue = Eligible customers * AI attach * AI price
```

Track production workflows, action volume, completion rate, renewal uplift, and budget conversion rather than treating pilot count as recurring revenue.

## 5. Earnings bridge

```text
Revenue = Sum(segment revenue)
Gross profit = Revenue * Gross margin
Operating income = Gross profit - Operating expenses
Net income = Operating income - Interest - Taxes
EPS = Net income / Diluted shares
```

Build revenue and margin from operational drivers before applying valuation. Keep valuation scenarios separate from operating scenarios to prevent double counting optimism or risk.
