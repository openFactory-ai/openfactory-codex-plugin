# Public directory submission

## Verified package and live service (2026-10-12)

The current upload is `dist/openfactory-1.0.5.zip` (SHA-256
`e06d55605e00784de0e3343a50f2c34837d8a7a0625e022b5c6c5dd5ffe026ad`).
Its contents match the source package, include both theme icons and all eight
review cases, and exclude reviewer credentials and private repository links.
The public WebM and MP4 demos return HTTP 200 and match the website source
files. The updated OAuth privacy policy, terms and contact pages are live.

The dedicated reviewer account passes password sign-in, browser-session
sign-in, OAuth dynamic registration with PKCE, and MCP initialization. The
live service exposes 173 tools, including every tool named in the positive
cases. Direct MCP checks cover Debian recipe browsing, recipe validation,
draft preparation, account build status and missing verification evidence. The
fresh reviewer draft is `a50a48bc-ca04-4a0d-9ad4-5f537dd4342a`; it stopped at
worktree preparation, with image inputs not started and no image or test runs.
After the check, the QA draft was cancelled to release its active reservation;
its record and history remain available. Platform administration
tools and caller-supplied identity arguments are absent. These checks do not
replace running the eight prompts in ChatGPT or the dashboard's automated scans.

The dashboard challenge token has been received and saved in the local
persistent service configuration. The local challenge endpoint returns HTTP
200 with the exact plaintext token. The public AWS frontend still returns
HTTP 404; its configuration update is queued behind the shared deployment
lock while another platform deployment drains active test sessions. A
persistent service will apply the token, complete the AWS rollout and check
the exact public response when the lock becomes available. Its result is
recorded in the maintainer's local evidence directory at
`../test-evidence/plugin-submission-20261012/domain-challenge-deployment.json`.
Domain verification in the dashboard remains pending. No OpenAI dashboard
submission or approval has been verified. This configuration change requires
no new plugin ZIP.

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
