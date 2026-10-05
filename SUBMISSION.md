# Public directory submission

Upload the release ZIP at https://platform.openai.com/plugins using a verified
OpenFactory publishing organization. The uploader needs organization ownership
or Apps Management write access. Choose **With MCP** and connect:

```
https://console.openfactory.tech/api/mcp-stream/plugin/mcp
```

Use OAuth with dynamic client registration, public client authentication
(`none`), scope `openfactory`, authorization-code flow and PKCE S256.
The authorization server is
`https://console.openfactory.tech/api/mcp-oauth`. Discovery endpoints are:

- `https://console.openfactory.tech/.well-known/oauth-authorization-server/api/mcp-oauth`
- `https://console.openfactory.tech/.well-known/oauth-protected-resource/api/mcp-stream/plugin/mcp`

Complete the portal's ownership challenge on `console.openfactory.tech`.
OpenFactory's edge exposes `/.well-known/openai-apps-challenge` when the exact
portal-provided plaintext is configured as `OPENFACTORY_OPENAI_APPS_CHALLENGE`.
The challenge value comes from the publishing dashboard.

The dedicated OpenFactory reviewer account has a prepared Debian desktop
draft. It has no verified image; the evidence test must report that accurately.
Reviewer credentials are retained privately by the maintainer. Enter them
only in the secure dashboard fields, never in the ZIP or repository.

Attach the release's `openfactory-demo.mp4`. It shows real browser consent,
live MCP recipe browsing and validation, the prepared draft's status and
evidence, and browser revocation. Codex marketplace installation and native
OAuth login were also verified. ChatGPT installation and the full reviewer
prompts still need testing through the publisher dashboard.

The manifest supplies five positive and three negative test cases. Run them
with the reviewer account, resolve automated scan findings, and submit for
review. After approval, choose publication. A GitHub release alone does not
publish the plugin in the universal directory.
