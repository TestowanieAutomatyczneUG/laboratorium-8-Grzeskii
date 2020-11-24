import unittest

from sample.GetMeal import GetMeal


class TestGetMeal(unittest.TestCase):

    def setUp(self):
        self.temp = GetMeal()

    def test_get_meal_positive_arrabiata(self):
        expected = self.temp.getter("Arrabiata")
        self.assertEqual(len(expected), 1)

    def test_get_meal_positive_spaghetti(self):
        expected = self.temp.getter("Spaghetti")
        self.assertEqual(len(expected), 1)
    
    def test_get_meal_error_str(self):
        expected = self.temp.getter("Arabarabrara")
        self.assertEqual(expected, "This meal doesn't exist!")
    
    def test_get_meal_error_num(self):
        expected = self.temp.getter(32131)
        self.assertEqual(expected, "This meal doesn't exist!")

if __name__ == '__main__':
    unittest.main()
