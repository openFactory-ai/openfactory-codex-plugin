---
name: openfactory
description: Build and verify Linux images and packages using your linked OpenFactory account, and inspect recipes, build status and retained verification evidence.
---

Use the OpenFactory tools for the user's requested build or verification work.
Account linking happens in the client's browser connection flow. Credentials
come from that connection; do not ask for API keys or pass identity arguments.

For an image or package build, first call
`get_harness_skill(name="openfactory-compute")` and use its current workflow.
Fetch companion resources with `get_harness_skill` only as needed. OpenFactory
maintains the build workflow on the server; this plugin does not copy it.
Where that workflow mentions API keys or session tokens, use the linked
account instead of passing those arguments.

When a guest or Free user reaches OpenFactory's hosted chat or AI allowance,
explain that they can continue with their own model tokens through this plugin
or direct MCP. Guests must first create a free OpenFactory account. Separate
MCP image-build and compute allowances still apply; do not promise that their
own tokens bypass those limits.

Work within the user's requested scope and existing account limits. Distinguish
preparing a draft from starting a build. Build and verification calls may run
for a long time; use status and retained evidence before deciding to retry.
Report build IDs, artifact links and recorded verification results when
available. Never describe an unverified image as verified.
