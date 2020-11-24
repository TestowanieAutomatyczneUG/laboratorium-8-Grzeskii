import unittest

from sample.GetMeal import GetMeal


class TestSimple(unittest.TestCase):

    def setUp(self):
        self.temp = GetMeal()

    def test_add_one(self):
        expected = self.temp.getter("Arrabiata")
        self.assertEqual(len(expected), 1)

if __name__ == '__main__':
    unittest.main()
