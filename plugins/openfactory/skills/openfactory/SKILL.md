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
For setup, install or how-to questions about OpenFactory itself, fetch
https://docs.openfactory.tech/llms.txt (index) or
https://docs.openfactory.tech/llms-full.txt (all docs).

Work within the user's requested scope and existing account limits. Distinguish
creating a draft build from building its image.

You drive the build: the recipe delivers packages and repositories, and you
write everything else the image needs with `write_build_config`. Check the
booted test machine against what the user asked for, fix every difference in one
change, and build again until it all holds. A defect you can still edit is not a
reason to stop, and a verification run the platform itself failed says nothing
about the image. The guide has the full list of what you can change and when to
stop.

Build and verification calls start work that continues on the server; poll
status, and read the retained evidence before deciding what to change.
Report build IDs, artifact links and recorded verification results when
available. Never describe an unverified image as verified.
