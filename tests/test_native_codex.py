"""Exercise the installed plugin through Codex, without account credentials."""

import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import tempfile
import threading
import unittest


ROOT = Path(__file__).resolve().parents[1]
CODEX = os.environ.get("CODEX_BINARY") or shutil.which("codex")


@unittest.skipUnless(CODEX, "Codex CLI is required for the native plugin test")
class NativeCodexPluginTest(unittest.TestCase):
    def test_installed_plugin_discovers_openfactory_mcp_server(self):
        with tempfile.TemporaryDirectory() as home:
            codex_home = Path(home) / ".codex"
            codex_home.mkdir()
            env = dict(os.environ, HOME=home, CODEX_HOME=str(codex_home))
            for args in [
                ["plugin", "marketplace", "add", str(ROOT), "--json"],
                ["plugin", "add", "openfactory@openfactory", "--json"],
            ]:
                subprocess.run(
                    [CODEX, *args], env=env, check=True, capture_output=True,
                    text=True, timeout=30,
                )
            process = subprocess.Popen(
                [CODEX, "app-server"], env=env, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
            )
            replies = queue.Queue()

            def read_replies():
                for line in process.stdout:
                    replies.put(json.loads(line))

            threading.Thread(target=read_replies, daemon=True).start()

            def request(request_id, method, params):
                process.stdin.write(json.dumps({
                    "id": request_id, "method": method, "params": params,
                }) + "\n")
                process.stdin.flush()
                while True:
                    reply = replies.get(timeout=30)
                    if reply.get("id") == request_id:
                        self.assertNotIn("error", reply)
                        return reply["result"]

            try:
                request(1, "initialize", {
                    "clientInfo": {"name": "openfactory-plugin-test", "version": "1"},
                    "capabilities": {"experimentalApi": True},
                })
                process.stdin.write('{"method":"initialized","params":{}}\n')
                process.stdin.flush()
                plugin = request(2, "plugin/read", {
                    "marketplacePath": str(ROOT / ".agents/plugins/marketplace.json"),
                    "pluginName": "openfactory",
                })["plugin"]
                self.assertTrue(plugin["summary"]["installed"])
                self.assertTrue(plugin["summary"]["enabled"])
                self.assertEqual(plugin["mcpServers"], ["openfactory"])
            finally:
                process.terminate()
                process.communicate(timeout=10)


if __name__ == "__main__":
    unittest.main()
