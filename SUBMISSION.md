# Public directory submission

## Current package and service (2026-10-13)

The current upload is `dist/openfactory-1.0.6.zip` (SHA-256
`30e940d91f869fa0362c3a5321fbe603972945013a999dc4c31d56b827625414`). It
replaces 1.0.5: the draft-build review case now uses `create_build`, which the
plugin offers, instead of `prepare_harness_build`, which it no longer offers,
and the onboarding skill no longer discusses account tiers or allowances.

Domain verification passed on 2026-10-13. The challenge token is set both in
the local service configuration and in the public console's AWS container
environment; the public endpoint returns HTTP 200 with the exact token. The MCP
server is connected in the dashboard with OAuth.

The dashboard's automated scan then flagged the server instructions, several
annotations, descriptions written for other surfaces and multi-operation
tools. The service now publishes a 93-tool Linux image build-and-test surface
with its own instructions, one guest-agent tool per operation, corrected
annotations, and responses and a served build guide that never promote plans,
upgrades or checkout (monorepo `docs/guides/public-plugin.md`). After the
service deploy, rescan tools in the dashboard and upload this ZIP.

The reviewer demo predates these changes. It shows recipe browsing,
validation, a draft's status and evidence and browser revocation, which still
apply. The draft in it came from the tool the plugin no longer offers.

## Finish in the publishing dashboard

Upload the release ZIP at https://platform.openai.com/plugins using a verified
OpenFactory publishing organization. The uploader needs organization ownership
or Apps Management write access. Choose **With MCP** and connect:

```
https://console.openfactory.tech/api/mcp-stream/plugin/mcp
```

The packaged `mcp.json` declares OAuth with dynamic client registration and
the `openfactory` scope. The portal imports these settings from the ZIP;
check them under **MCPs** before connecting. Discovery supplies the OAuth
endpoints, public client authentication (`none`), authorization-code flow
and PKCE S256.
The authorization server is
`https://console.openfactory.tech/api/mcp-oauth`. Discovery endpoints are:

- `https://console.openfactory.tech/.well-known/oauth-authorization-server/api/mcp-oauth`
- `https://console.openfactory.tech/.well-known/oauth-protected-resource/api/mcp-stream/plugin/mcp`

The auth extension follows [OpenAI's MCP authentication format](https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication).
The public Agent Plugins 1.0.0 MCP JSON schema currently rejects per-server
extensions, including this documented OpenAI extension. Validate the imported
auth settings in the OpenAI portal; generic schema validation alone cannot
confirm submission compatibility.

Complete the portal's ownership challenge on `console.openfactory.tech`.
OpenFactory's edge exposes `/.well-known/openai-apps-challenge` when the exact
portal-provided plaintext is configured as `OPENFACTORY_OPENAI_APPS_CHALLENGE`.
The challenge value comes from the publishing dashboard.

The dedicated OpenFactory reviewer account has a prepared Debian desktop
draft. It has no verified image; the evidence test must report that accurately.
Reviewer credentials are retained privately by the maintainer. Enter them
only in the secure dashboard fields, never in the ZIP or repository.

Use the public website's [reviewer demo](https://openfactory.tech/proofs/openfactory-plugin-demo.webm).
It shows real browser consent,
live MCP recipe browsing and validation, the prepared draft's status and
evidence, and browser revocation. All supporting-content URLs must be publicly
accessible on OpenFactory's website; this repository is private. Codex marketplace installation and native
OAuth login were also verified. ChatGPT installation and the full reviewer
prompts still need testing through the publisher dashboard.

The manifest supplies five positive and three negative test cases. Run them
with the reviewer account, resolve automated scan findings, and submit for
review. After approval, choose publication. A GitHub release alone does not
publish the plugin in the universal directory.
