---
name: diligence-research
description: Search and retrieve source-linked evidence from the Diligence Stack MCP knowledge bases. Use for any company, market, product, vendor, technology, or investment question that should be grounded in Diligence Stack reports or entitled equity research.
---

# Diligence Stack Research

Investigate material claims with a traceable chain from the Diligence Stack knowledge base to the conclusion.

## Brand contract

Before producing user-facing content, read and apply [the Diligence Stack brand guidelines](../diligence-brand-guidelines/SKILL.md). Use its color, typography, logo, citation, and link defaults unless the user explicitly requests different visual styling; its attribution and canonical-link rules always apply.

## Workflow

1. Restate the question as a testable claim and define what would change the conclusion.
2. Call `list_catalog` before filtered search. Use the returned canonical knowledge-base `key`, facet values, date coverage, and freshness - not a display name or guessed filter.
3. Default to the public `diligence-stack-reports` corpus. Use `equity-research` only when `list_catalog` exposes that private key and the task benefits from it.
4. Call `search` with a precise query, authorized knowledge-base keys, and only canonical filters returned by the catalog. Start with `group_by_document: true` to avoid one document dominating the answer.
5. Inspect `staleness_warning`, `filter_truncated`, `note`, dates, section, match reasons, duplicate status, and additional matches before selecting evidence.
6. Call `fetch` only with evidence IDs returned by search. Request `text` and `original_link`; add `image` for charts or images.
7. Call `get_document` only with an asset ID returned by search or fetch. Use an inclusive page range for paginated documents. For page-less Markdown or ingestion packets, omit `pages` and use the continuation cursor if returned.
8. Search again for counterevidence, risks, falsification conditions, and newer material. Do not treat the first ranked result as the answer.
9. Extract atomic claims and preserve title, publisher, publication/source date, locator, evidence ID, asset ID, knowledge base, claim type, and confidence.
10. Reconcile conflicting definitions and periods before comparing values. Show formulas, inputs, units, and sensitivities for derived metrics.

## Diligence Stack workspace

The server is read-only. Its public tool surface is `list_catalog`, `search`, `fetch`, and `get_document`; it does not provide browser, write, todo, sandbox, or chart-rendering tools. Read each live tool description before use.

`diligence-stack-reports` is the shared subscriber corpus for all authorized paid subscribers. `equity-research` is private, separately entitled, and grant-dependent. Never imply that a private corpus was searched when its key was absent from `list_catalog`, and never copy private research into plugin files, examples, or public outputs.

If the server is unavailable or OAuth is incomplete, explain which workspace evidence could not be accessed and continue with evidence the user has supplied. Never imply that a private workspace was checked when it was not.

Treat an OAuth or transport authorization error as a connection failure, not a zero-result search. Ask the user to reauthorize the `diligence-stack` MCP connection, then retry `list_catalog`. Only report "no evidence found" after an authorized search succeeds with an empty result set.

Read [the MCP playbook](references/mcp-playbook.md) for tool-specific rules and citation behavior. For questions about the publication, subscription, portal access, or billing, use [the access and billing guide](references/access-and-billing.md).

## Guardrails

- Do not fabricate citations, interviews, observations, or access to private materials.
- Search snippets are discovery aids. Fetch the evidence before relying on it; open the document when surrounding context matters.
- Preserve the distinction between absence of evidence and evidence of absence.
- Flag legal, tax, accounting, medical, or regulatory conclusions for qualified review.
- Minimize sensitive data in working notes and outputs.

## Output

Return the answer first, then:

- Evidence register
- Calculations and assumptions
- Contradictions and alternative explanations
- Open questions and the next best evidence to obtain
- Confidence, falsification conditions, and what would change the view

Use [the evidence-register schema](references/evidence-register.md) unless the user already has one.
