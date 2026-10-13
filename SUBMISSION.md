# Public directory submissions

OpenAI (ChatGPT and Codex) first; the Claude directory is at the end.

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

The reviewer demo was re-recorded on 2026-10-13 against this deployed surface.
It follows the review cases: Codex's browser consent, recipe browsing and
validation, a draft created with `create_build`, its status and evidence, and
browser revocation, after which the same token gets HTTP 401.

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

The dedicated OpenFactory reviewer account has Debian desktop drafts; the
newest was created in the demo. None has a verified image; the evidence test
must report that accurately.
Reviewer credentials are retained privately by the maintainer. Enter them
only in the secure dashboard fields, never in the ZIP or repository.

Use the public website's [reviewer demo](https://openfactory.tech/proofs/openfactory-plugin-demo.webm).
It shows real browser consent,
live MCP recipe browsing and validation, a draft created with `create_build`,
its status and evidence, and browser revocation. All supporting-content URLs must be publicly
accessible on OpenFactory's website. Codex marketplace installation and native
OAuth login were also verified. ChatGPT installation and the full reviewer
prompts still need testing through the publisher dashboard.

The manifest supplies five positive and three negative test cases. Run them
with the reviewer account, resolve automated scan findings, and submit for
review. After approval, choose publication. A GitHub release alone does not
publish the plugin in the universal directory.

## Claude directory (2026-10-13)

Anthropic lists remote MCP servers and plugins in one directory. Submit both
from the developer portal at https://claude.ai/directory/manage → **Submit
new**, signed in to the claude.ai organization that should own the listings
(paid plan; on Team or Enterprise only an Owner can submit). Submit the MCP
connector first, then the plugin bundle, and pair them. There is no domain
challenge. Requirements: https://claude.com/docs/connectors/building/review-criteria
and https://claude.com/docs/plugins/pre-submission-checklist.

Before submitting, add the server as a custom connector in claude.ai
(Settings → Connectors → Add custom connector, the URL below) and run the
tools from a chat; the **Test & launch** step asks you to confirm this.

### 1. MCP connector

| Step | Answer |
| --- | --- |
| Connection | `https://console.openfactory.tech/api/mcp-stream/plugin/mcp` (one URL for all users) |
| Tools | Synced from the server: every tool has a title and a read-only or destructive hint (monorepo `elster-terminal-backend/app/mcp/plugin_server.py`). |
| Server name | OpenFactory |
| One-liner | Build custom Linux OS images from recipes and test them in virtual machines, in your OpenFactory account. |
| Description | See below. |
| Categories | Developer tools (add Infrastructure or DevOps if offered) |
| Documentation URL | https://docs.openfactory.tech/en/reference/mcp |
| Privacy policy URL | https://openfactory.tech/privacy |
| Support contact | support@openfactory.tech |
| Icon | `plugins/openfactory/assets/icon.png` (512×512) |
| Slug | `openfactory` (permanent once published) |
| Use cases | Build a custom Linux image from a recipe; verify an image in a test VM and review the evidence; diagnose a failed build or an installed system that does not boot. |
| Prerequisites | An OpenFactory account (https://console.openfactory.tech). Builds and VMs use that account's compute allowance. |
| Reads or writes | Both |
| Company | OpenFactory, https://openfactory.tech, primary contact: the maintainer |
| Authentication | OAuth with dynamic client registration (public client, PKCE S256, scope `openfactory`) |
| Data handling | Our own first-party API. No personal health data. No sponsored content. |
| Test & launch | See below; enter the reviewer credentials only in the portal's secure fields. |
| Compliance | Seven acknowledgments; the maintainer reads and accepts them. |

Description (under 2,000 characters):

> OpenFactory builds custom Linux operating-system images and tests them in
> virtual machines. This connector lets Claude work in your OpenFactory
> account: browse and validate recipes, create a build, compile and verify
> the image, drive the test VM's desktop and inspect it through its guest
> agent, record verification evidence, and get the download link for the
> finished ISO.
>
> Typical uses:
> - Start from an existing recipe or write your own, and set the image's
>   packages, services and desktop.
> - Build the image and read its status, test results and retained evidence.
> - Open a verification session on the test VM: take screenshots, click and
>   type in its desktop, run commands through the guest agent and record each
>   requirement you checked.
> - Inspect the disk of an installed system that failed to boot.
> - Manage lab networks of VMs, internal package repositories and OBS package
>   builds.
>
> Every call acts on the signed-in account only. Read-only tools are marked
> read-only; tools that delete, stop or overwrite resources are marked
> destructive, so Claude asks before running them. Builds and VMs use your
> account's compute allowance.

Test & launch instructions:

> 1. Add the connector and choose Connect. An OpenFactory sign-in page opens.
> 2. Sign in with the reviewer account below, review the `openfactory`
>    permission and choose Allow.
> 3. Try these prompts:
>    - "Show me the available Debian desktop recipes." (list_recipes,
>      list_recipe_categories; creates nothing)
>    - "Validate this recipe before building it: {"name":"Review Debian",
>      "base_image":"debian-bookworm","os":{"features":["desktop-xfce","firefox"]}}"
>      (validate_recipe)
>    - "Create a Debian desktop build from an available template. Return the
>      draft build ID and stop before building the image." (create_build)
>    - "List my recent builds and show the status of the newest one."
>      (list_builds, get_build_status)
>    - "Summarize the retained evidence for my newest build and explain
>      whether it is verified." (get_build_evidence, list_test_runs)
> 4. build_image compiles and tests a real image; it takes several minutes
>    and counts against the account's monthly build allowance.
> 5. Disconnecting the connector in Claude revokes the token.

### 2. Plugin bundle

The plugin folder `plugins/openfactory` serves both directories: Claude reads
`.claude-plugin/plugin.json` (the remote MCP server above plus listing links)
and `README.md`, Codex reads `plugin.json` and `mcp.json`, and both load
`skills/openfactory`. `claude plugin validate --strict ./plugins/openfactory`
passes. The repository is public, so the portal needs only your GitHub
account connected on claude.ai with push access.

| Step | Answer |
| --- | --- |
| Repository | `openFactory-ai/openfactory-codex-plugin` |
| Plugin path | `plugins/openfactory` |
| Branch | `main` |
| Listing details | Read from `plugin.json` and `README.md`; change them there and re-validate. |
| Personal data | Read through its declared connector only (the signed-in account's builds, recipes, VMs and evidence); the plugin itself stores nothing. |
| Other services | None beyond the declared connector. |
| Retention | The plugin keeps nothing; OpenFactory retains account data as its privacy policy describes. |
| Under 18 | No (OpenFactory is not intended for children under 16). |
| Compliance | Contact email, four acknowledgments. |
| Updates | GitHub push webhook (needs repository admin), or scheduled check only. |

Raise `version` in `.claude-plugin/plugin.json` with every release the
directory should pick up.
