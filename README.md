# Diligence Stack Marketplace

A dual-platform plugin marketplace for **The Diligence Stack by Creative Strategies**.

[**Install Diligence Core in Claude Cowork**](https://claude.ai/desktop/customize/plugins/new?marketplace=mweinbach%2Fdiligence-stack-marketplace&plugin=diligence-core)

## What is The Diligence Stack?

The Diligence Stack is a Creative Strategies research publication on Substack covering the core fundamentals of companies, technologies, and industries. It is designed as a due-diligence resource for the full technology stack: semiconductors, infrastructure, cloud platforms, software, adoption, business models, and competitive positioning.

The research begins with AI because AI increasingly connects every layer of the technology economy, but its scope extends wherever understanding a company or industry requires technical, operational, market, and economic context. The goal is not a rating or price target. It is to help readers understand how the system works and bring that understanding into their own underwriting and decision-making.

The same skill source works across Codex/ChatGPT and Claude Cowork/Claude Code; only the marketplace and plugin manifests are platform-specific.

## Access tiers and billing

| Access level | What it includes | Portal and MCP |
|---|---|---|
| Free reader | The opening 600–800 words of each published report. | Not included. |
| Paid subscriber | Full subscriber research and archive, including the Diligence Stack subscriber portal and the shared `diligence-stack-reports` MCP knowledge base. | Included after subscriber verification and OAuth authorization. |
| Private entitlement | The private `equity-research` corpus for specifically approved accounts. | Appears only when the account's OAuth grant includes it; it is not promised as part of ordinary paid access. |

As of June 19, 2026, direct web subscription metadata lists **$300/month or $3,000/year in USD**. Pricing, taxes, currencies, promotions, team terms, and app-store pricing can change, so [check the live subscription page](https://www.thediligencestack.com/subscribe) before purchase.

Installing this marketplace does not create or include a Diligence Stack subscription. Subscription billing is handled by The Diligence Stack/Substack; the portal verifies the subscriber's email or passkey, and OAuth authorizes MCP access. Codex or Claude plans and usage are billed separately by their respective providers.

See [access and billing guidance](plugins/diligence-core/skills/diligence-research/references/access-and-billing.md) for the exact user-facing language.

## Included plugin

| Plugin | Skills | Purpose |
|---|---|---|
| `diligence-core` | 14 research, modeling, monitoring, and synthesis skills | Search source-linked evidence; build company, market, competitive, earnings, and model outputs; prepare interviews; find exhibits; audit claims; and monitor theses. |

See [all supported use cases and example prompts](docs/use-cases.md).

## Diligence Stack connection

The plugin bundles the remote Streamable HTTP MCP endpoint:

```text
https://portal.thediligencestack.com/mcp
```

The endpoint advertises OAuth protected-resource metadata and the read scopes `kb:search`, `kb:fetch`, and `kb:read`. Codex and Claude perform the OAuth flow natively, so the repository contains no token, client secret, or static authorization header. The subscriber `diligence-stack-reports` corpus is the default; the private `equity-research` corpus appears only for separately entitled OAuth grants.

## Repository layout

```text
.agents/plugins/marketplace.json       # Codex marketplace catalog
.claude-plugin/marketplace.json        # Claude marketplace catalog
plugins/diligence-core/
  .codex-plugin/plugin.json            # Codex / ChatGPT manifest
  .claude-plugin/plugin.json            # Claude Cowork / Code manifest
  .mcp.json                              # Shared remote MCP configuration
  skills/                                # Shared Agent Skills
scripts/                                 # Validation and Cowork packaging
```

## Install locally

### Codex / ChatGPT

From the repository root:

```powershell
codex plugin marketplace add .
codex plugin marketplace list
```

Then open `/plugins` in Codex, select **Diligence Stack**, and install **Diligence Core**. Start a new thread after installation.

When prompted, authorize the Diligence Stack connection. If Codex needs a manual retry, run:

```powershell
codex mcp login diligence-stack
```

### Claude Code

From the repository root:

```powershell
claude plugin marketplace add .
claude plugin install diligence-core@diligence-stack
```

Authorize Diligence Stack when Claude prompts during installation or first use. Use `/mcp` to inspect or retry the connection.

### Claude Cowork

Use the one-click installer:

[**Install Diligence Core in Claude Cowork**](https://claude.ai/desktop/customize/plugins/new?marketplace=mweinbach%2Fdiligence-stack-marketplace&plugin=diligence-core)

The link opens Claude Desktop's plugin installer and provides a browser fallback. It adds the `mweinbach/diligence-stack-marketplace` marketplace and selects `diligence-core` for installation.

For manual or offline distribution, Anthropic uses the same `.claude-plugin` bundle format for Cowork and Claude Code. Build the distributable zip:

```powershell
npm run package:cowork
```

The archive is written to `dist/diligence-core-0.3.0.zip` with the plugin manifest at the archive root.

## Publish from GitHub

After pushing this repository, replace `<owner>` below with the GitHub owner:

```powershell
codex plugin marketplace add <owner>/diligence-stack-marketplace
claude plugin marketplace add <owner>/diligence-stack-marketplace
claude plugin install diligence-core@diligence-stack
```

Relative plugin paths require installing the marketplace from a Git repository or local checkout, not from a direct URL to a standalone JSON file.

## Validate and package

```powershell
npm run validate
npm run package:cowork
```

The validation suite also checks the skill evaluation scenarios in `evals/scenarios.json`.

If the platform CLIs are installed, also run:

```powershell
claude plugin validate .
claude plugin validate ./plugins/diligence-core --strict
```

## Add another plugin

1. Create `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
2. Add matching `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` manifests.
3. Add the plugin to both marketplace catalogs.
4. Keep the folder name, both manifest names, and both manifest versions identical.
5. Run `npm run validate` and package-test the Claude bundle.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the release checklist.

The live MCP review and server-side recommendations are in [docs/mcp-review.md](docs/mcp-review.md).

## Sources

- [OpenAI: Build plugins](https://developers.openai.com/codex/plugins/build)
- [Anthropic: Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
- [Anthropic knowledge-work plugins](https://github.com/anthropics/knowledge-work-plugins)
- [The Diligence Stack: About](https://www.thediligencestack.com/about)
- [The Diligence Stack: Subscribe](https://www.thediligencestack.com/subscribe)

## License

MIT
