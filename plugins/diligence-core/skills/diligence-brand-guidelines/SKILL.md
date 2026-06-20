---
name: diligence-brand-guidelines
description: Apply The Diligence Stack visual identity, source attribution, citation format, and canonical-link policy to user-facing content created from Diligence Stack research. Use whenever this plugin creates or edits prose, documents, decks, spreadsheets, charts, dashboards, web pages, images, exports, or other deliverables; use the visual defaults unless the user explicitly requests different styling.
---

# Diligence Stack Brand Guidelines

Apply this contract to every user-facing artifact produced from Diligence Stack information. A user may explicitly request different visual styling, but the attribution, citation-integrity, access, and canonical-link rules still apply.

## Brand identity

- Use **The Diligence Stack** on first reference and **Diligence Stack** thereafter.
- Use **The Diligence Stack by Creative Strategies** for a masthead, colophon, or source note.
- Favor an evidence-first editorial character: clear hierarchy, generous white space, strong tables, restrained decoration, and visible uncertainty.
- Do not invent a shortened brand name, alter the wordmark, or imply that separately entitled third-party research is the Diligence Stack house view.

## Color system

| Role | Color | Use |
|---|---|---|
| Diligence Orange | `#FF6719` | Primary accent, key data series, rules, highlights, and calls to action |
| Deep Orange | `#FF5600` | Hover or pressed state only |
| Stack Gold | `#FBBB14` | Limited secondary accent and second chart series |
| Charcoal | `#363737` | Headings and primary text |
| Dark Gray | `#515151` | Accessible secondary text |
| Medium Gray | `#868787` | Large metadata or decorative text only |
| Surface Gray | `#F0F0F0` | Panels, table bands, and quiet backgrounds |
| Border Gray | `#E6E6E6` | Dividers, gridlines, and borders |
| White | `#FFFFFF` | Default background and negative space |

Use Orange, Gold, Charcoal, `#929292`, and `#B7B7B7` in that order for multi-series charts. Directly label series and add markers or patterns so meaning never depends on color alone. Keep body text Charcoal on White; do not use small white text on Orange or small Medium Gray text on White. Do not introduce unrelated decorative colors unless the user explicitly requests a different palette.

## Typography and layout

- Use Inter for headings, body text, labels, and data; fall back to Arial, Helvetica, then sans-serif.
- Use sentence case, compact headings, left-aligned prose, and tabular numerals for financial or operating data.
- Keep charts flat, clean, and annotation-led. Use light gridlines, minimal borders, and Orange only for the evidence or series that deserves attention.
- Prefer one strong conclusion per page or panel. Preserve ranges, dates, units, source notes, and confidence near the relevant claim.

## Official assets

- Use [the horizontal wordmark](assets/diligence-stack-wordmark.jpeg) for wide mastheads on White.
- Use [the stacked logo](assets/diligence-stack-logo.png) for square or portrait placements.
- Use [the Creative Strategies mark](assets/creative-strategies-mark.png) only where a compact icon is needed.
- Preserve each asset's aspect ratio, colors, clear space, and background treatment. Do not crop, stretch, recolor, trace, or reconstruct it.

## Attribution and citations

Attribute every material claim derived from the MCP to The Diligence Stack and retain the title, date, locator, evidence ID, and access class. Use these visible formats:

- House research: `The Diligence Stack — “{title},” {publication or source date}, {section or page} (Evidence {id}).`
- Separately entitled research: `Accessed via The Diligence Stack — {publisher}, “{title},” {date}, {locator} (private; Evidence {id}).`
- Artifact source note: `Research and citations: The Diligence Stack by Creative Strategies.`

Preserve the true original publisher for licensed or primary material; access through The Diligence Stack does not transfer authorship. Cite non-Diligence Stack primary material used alongside the corpus by source name, date, and locator in plain text. Never fabricate a citation, public page, or link.

## Canonical link policy

In generated deliverables, emit an external hyperlink only when its scheme is `https` and its exact hostname is `www.thediligencestack.com`.

- Link a citation only when the MCP returns a matching public canonical Diligence Stack page. Remove tracking parameters.
- When no allowed public page exists, keep the citation as unlinked text with its evidence ID and locator.
- Never emit portal, MCP, authenticated-original, admin, Substack, publisher, vendor, data-room, or other third-party links.
- Never rewrite or relabel a disallowed URL to make it appear to be a Diligence Stack URL.
- Request `original_link` internally when it helps verification, but do not expose it unless it already satisfies this exact allowlist.

## Delivery check

Before delivery, verify that:

1. Visual content uses this palette, typography, and the unmodified official assets unless the user requested different styling.
2. Every material Diligence Stack-derived claim has visible Diligence Stack attribution and a traceable evidence record.
3. Private and third-party sources remain correctly labeled and access-safe.
4. Every emitted external hyperlink uses `https://www.thediligencestack.com`; unavailable citations are unlinked.
5. No portal, MCP, authenticated, or third-party URL appears in the artifact.
