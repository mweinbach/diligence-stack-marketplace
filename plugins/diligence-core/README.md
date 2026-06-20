# Diligence Core

A shared Codex, ChatGPT, Claude Code, and Claude Cowork plugin for **The Diligence Stack by Creative Strategies**.

The Diligence Stack is a Substack research publication covering the core fundamentals of companies and industries across the technology stack. It focuses on AI and the layers AI connects—semiconductors, infrastructure, cloud, platforms, software, customer adoption, business models, and competitive position—while extending to any market where full-stack diligence matters.

It connects to the private subscriber portal's MCP server at `https://portal.thediligencestack.com/mcp`. The server uses OAuth, so each user signs in through the client during installation or first use; no client secret or access token is stored in this repository. Installing the plugin does not grant a subscription.

It includes fourteen skills:

- `diligence-plan` scopes the decision, hypotheses, workstreams, and evidence requests.
- `diligence-research` operates the catalog-first MCP search, fetch, and document workflow.
- `diligence-synthesis` turns the evidence set into a recommendation, risk register, and decision memo.
- `company-diligence` creates vendor and company packets with reasoning maps, metrics, watch items, and falsification conditions.
- `market-diligence` creates market primers with architecture, value chains, bottlenecks, adoption paths, and value pools.
- `evidence-audit` grades claim quality, traceability, freshness, and decision usefulness.
- `equity-research-brief` compares the Diligence Stack house view with separately entitled private equity research when the user's OAuth grant permits it.
- `build-diligence-model` converts research into driver-based models, scenarios, sensitivities, and evidence-linked assumptions.
- `track-investment-thesis` maintains a living thesis, monitoring dashboard, catalysts, and falsification register.
- `prepare-earnings` supports pre-earnings preparation and post-earnings thesis/model updates.
- `map-competitive-landscape` maps ecosystem roles, control points, bottlenecks, substitutes, and value pools.
- `find-research-gaps` prioritizes missing evidence by decision impact and value of information.
- `prepare-management-meeting` creates high-signal questions for management, customers, suppliers, and experts.
- `find-research-exhibits` finds and validates charts, tables, scorecards, and diagrams from the knowledge base.

The subscriber `diligence-stack-reports` knowledge base is the default after paid subscriber verification. The private `equity-research` corpus requires a separate entitlement, is discovered at runtime, and is never assumed, copied into this repository, or required for the other skills.

See [access and billing](skills/diligence-research/references/access-and-billing.md) before publishing installation or upgrade instructions.

See the repository's [use-case map](../../docs/use-cases.md) for example prompts and the future roadmap.

The plugin's company and market frames are grounded in the live Diligence Stack corpus while remaining reusable across covered sectors.

This plugin supports research and analysis; it does not replace qualified legal, tax, accounting, medical, or regulatory advice.
