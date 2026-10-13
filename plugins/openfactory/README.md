# OpenFactory

OpenFactory builds custom Linux operating-system images from recipes and tests
them in virtual machines. This plugin connects Claude to your OpenFactory
account so you can browse and validate recipes, create builds, compile and
verify images, drive and inspect the test VMs, and download finished ISOs.

## What the plugin contains

- One remote MCP server, `https://console.openfactory.tech/api/mcp-stream/plugin/mcp`,
  operated by OpenFactory. You sign in with your OpenFactory account through
  OAuth 2.0 (authorization code with PKCE); no API key is entered or stored by
  the plugin, and no tool takes credentials.
- One skill, `openfactory`, that tells Claude how to use those tools. For an
  image or package build it asks Claude to load OpenFactory's current build
  workflow from the same server with the `get_harness_skill` tool.

The plugin runs no local code: no hooks, scripts, commands or local servers.

## What is sent where

Every tool call goes to OpenFactory's MCP server above and acts only on the
signed-in account: its recipes, builds, test runs, VMs, labs and repositories.
The plugin sends nothing to any other service and does not read your chat
history or local files. Read-only tools are annotated as such; tools that
delete, stop or overwrite resources are marked destructive, so Claude asks
before running them. Builds and VMs use your account's compute allowances.

## Example prompts

- "Show me the available Debian desktop recipes."
- "Create a Linux image build draft for my requirements."
- "Summarize the verification evidence for my latest build."

## Links

- Documentation: https://docs.openfactory.tech/en/reference/mcp
- Support: https://openfactory.tech/contact
- Privacy policy: https://openfactory.tech/privacy
- Terms of service: https://openfactory.tech/terms

## License

MIT. See `LICENSE`.
