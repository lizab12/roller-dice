import unittest
from app import app

class DiceTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_roll(self):
        response = self.client.get('/roll')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(1 <= data["result"] <= 6)

if __name__ == '__main__':
    unittest.main()
