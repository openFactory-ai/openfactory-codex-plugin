# OpenFactory plugin

Use OpenFactory’s existing public MCP service from Codex and ChatGPT to build
Linux images and packages, run virtual machines and inspect verification
evidence. The plugin connects your existing account with browser OAuth and
loads OpenFactory’s current build guidance from the server.

## Install in Codex

```sh
codex plugin marketplace add openFactory-ai/openfactory-codex-plugin
codex plugin add openfactory@openfactory
```

Enable the plugin and follow the account connection prompt. Sign in to
OpenFactory, review the permissions and choose **Allow**. No API key, Node
bridge or local MCP server is needed. Your account’s existing permissions and
compute allowances apply; builds and cloud actions can incur charges.

If you reach OpenFactory's hosted chat or AI allowance, you can continue with
your own model tokens through this plugin or [direct MCP](https://docs.openfactory.tech/en/reference/mcp).
Guests need to create a free OpenFactory account first. Separate MCP build
and compute allowances still apply; supplying tokens does not reset them.

If your client does not prompt automatically, run:

```sh
codex mcp login openfactory --scopes openfactory --oauth-client-registration dcr
```

For development, clone this repository and add its directory with
`codex plugin marketplace add /absolute/path/to/openfactory-codex-plugin`.

## Use

Try “Show me the available Debian desktop recipes,” “Prepare a Linux image
build for my requirements,” or “Summarize verification evidence for my latest
build.” Select OpenFactory in the host’s plugin menu when needed.

The MCP endpoint is
`https://console.openfactory.tech/api/mcp-stream/plugin/mcp`.
The plugin reuses the existing public tool handlers, with OAuth identity and
action annotations. Credential-entry and platform-administration tools are
excluded. Account authorization is enforced by OpenFactory.

Manage or revoke connections at
[Connected clients](https://build.openfactory.tech/auth/connections). Revocation
immediately removes client access and preserves your account’s builds and
repositories. Connections expire after 30 days; reconnect when prompted.

## ChatGPT and public distribution

The portable package is under [`plugins/openfactory`](plugins/openfactory).
Release ZIPs have `plugin.json` at their root and can be uploaded through the
[OpenAI plugin submission portal](https://platform.openai.com/plugins).
Public directory availability depends on OpenAI review and publication. The
GitHub marketplace is a separate installation source.

The manifest includes five positive and three negative reviewer test cases.
See [submission preparation](SUBMISSION.md) for the remaining portal steps.
The [release demo](https://github.com/openFactory-ai/openfactory-codex-plugin/releases/download/v1.0.0/openfactory-demo.mp4)
shows browser consent, live recipe validation, build status, retained evidence,
and account revocation.

[Website](https://openfactory.tech) · [Support](https://openfactory.tech/contact)
· [Privacy](https://openfactory.tech/privacy) · [Terms](https://openfactory.tech/terms)

MIT licensed. Maintained by OpenFactory.
