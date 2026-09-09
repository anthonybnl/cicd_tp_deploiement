import unittest
import requests

TEST_URL = "http://localhost:3000"

class TestE2E(unittest.TestCase):

    def test_root_404(self):
        res = requests.get(f"{TEST_URL}/", timeout=5)
        self.assertEqual(res.status_code, 404)

    def test_healthcheck(self):
        res = requests.get(f"{TEST_URL}/health", timeout=5)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json(), {"message": "l'api fonctionne correctement", "status": "ok"}
        )
