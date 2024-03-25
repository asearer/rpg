import unittest
from utils import generate_random_name

class TestUtils(unittest.TestCase):
    def test_generate_random_name(self):
        name = generate_random_name()
        self.assertTrue(isinstance(name, str))
        self.assertNotEqual(name, "")

if __name__ == '__main__':
    unittest.main()
