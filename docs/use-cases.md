# Diligence Stack skill and use-case map

The MCP is most useful as a research operating system: discover evidence, convert it into a structured analytical artifact, identify what remains uncertain, and monitor what changes.

## Available workflows

| Job | Skill | Example prompt |
|---|---|---|
| Search the corpus | `diligence-research` | “Find the strongest evidence on AI networking control points and show the source trail.” |
| Scope an investigation | `diligence-plan` | “Build a diligence plan for evaluating this infrastructure vendor.” |
| Build a company packet | `company-diligence` | “Create a source-linked company packet for AMD.” |
| Build a market primer | `market-diligence` | “Map the liquid-cooling market, adoption path, bottlenecks, and value pools.” |
| Compare competitors | `map-competitive-landscape` | “Compare where Broadcom, Marvell, Credo, and Astera control the AI networking stack.” |
| Build a model | `build-diligence-model` | “Turn this neocloud thesis into a capacity, revenue-per-MW, and gross-profit model.” |
| Track a thesis | `track-investment-thesis` | “Create a quarterly tracker with leading signals and falsification conditions.” |
| Prepare for earnings | `prepare-earnings` | “Build a pre-earnings brief with KPI thresholds and thesis-moving questions.” |
| Compare private research | `equity-research-brief` | “Show where entitled analyst research agrees and disagrees with the house view.” |
| Audit evidence | `evidence-audit` | “Audit whether this AI ROI claim is supported by operating evidence.” |
| Find research gaps | `find-research-gaps` | “What would we still need to prove before underwriting this scenario?” |
| Prepare a meeting | `prepare-management-meeting` | “Prepare 12 questions for management that resolve the largest model uncertainties.” |
| Find exhibits | `find-research-exhibits` | “Find the best charts for an AI infrastructure market deck.” |
| Write the decision output | `diligence-synthesis` | “Turn this evidence and model into a decision-ready memo.” |

## End-to-end plays

### Company initiation

`company-diligence` → `map-competitive-landscape` → `build-diligence-model` → `find-research-gaps` → `prepare-management-meeting` → `track-investment-thesis`

### Market deep dive

`market-diligence` → `map-competitive-landscape` → `find-research-exhibits` → `build-diligence-model` → `evidence-audit` → `diligence-synthesis`

### Quarterly research loop

`prepare-earnings` → `diligence-research` → `build-diligence-model` → `track-investment-thesis` → `diligence-synthesis`

### Thesis challenge

`evidence-audit` → `find-research-gaps` → `prepare-management-meeting` → `track-investment-thesis`

## High-value future additions

These are good candidates once the core workflows have real usage data:

1. **Portfolio exposure map:** connect holdings to shared technology, customer, supply, power, financing, and architecture risks.
2. **Supply-chain stress test:** propagate a constraint or architecture shift across upstream and downstream beneficiaries.
3. **Research revision detector:** compare newly indexed evidence with prior reports and flag changed claims, metrics, or confidence.
4. **Benchmark extractor:** normalize recurring operating metrics across vendor packets into a comparable table.
5. **Survey and transcript synthesis:** combine user-provided primary research with knowledge-base context while preserving respondent provenance.
6. **Report and deck builder:** turn approved analysis and exhibits into branded subscriber deliverables.
7. **Corpus health audit:** detect stale coverage, missing metadata, duplicate documents, weak source links, and under-covered categories; this requires an admin/metadata tool surface not currently exposed.
8. **Team research workflow:** assign gaps, record review status, and publish updates; this requires write tools or an external project system.

## Product principles

- Keep retrieval separate from interpretation and interpretation separate from recommendation.
- Preserve evidence IDs, locators, dates, claim types, and confidence through every artifact.
- Use the shared subscriber corpus by default and private equity research only when explicitly granted.
- Treat models as transparent argument maps, not precision machines.
- Make every important thesis falsifiable and monitorable.
- Distinguish an OAuth failure from a valid empty search.
