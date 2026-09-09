import os
from pathlib import Path
import sys
import unittest
from fastapi.testclient import TestClient

BASE_PATH = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(BASE_PATH))

from src.api import app


class TestEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = TestClient(app)

    def test_root_404(self):
        response = self._client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_healthcheck(self):
        response = self._client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "l'api fonctionne correctement", "status": "ok"},
        )
