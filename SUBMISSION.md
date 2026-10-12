# Public directory submission

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
