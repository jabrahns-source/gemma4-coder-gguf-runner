"""Smoke checks for the Gemma 4 runner config. Does not download weights."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONF = ROOT / "config" / "server.conf"
DOCKERFILE = ROOT / "docker" / "Dockerfile"


class ConfigSmokeTest(unittest.TestCase):
    def test_server_conf_has_bind_and_model_slot(self):
        text = CONF.read_text(encoding="utf-8")
        self.assertGreater(len(text), 200)
        lowered = text.lower()
        self.assertTrue("port" in lowered or "host" in lowered)
        self.assertNotIn("placeholder", lowered)

    def test_dockerfile_does_not_vendor_weights(self):
        text = DOCKERFILE.read_text(encoding="utf-8")
        self.assertIn("FROM", text)
        self.assertNotIn(".gguf", text.lower())


if __name__ == "__main__":
    unittest.main()
