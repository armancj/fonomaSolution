import unittest

from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
