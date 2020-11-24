import unittest

from sample.GetMealById import GetMealById


class TestGetMeal(unittest.TestCase):

    def setUp(self):
        self.temp = GetMealById()

    def test_get_meal_by_id_positive_str(self):
        expected = self.temp.getter_id("52772")
        self.assertEqual(len(expected), 1)

    def test_get_meal_by_id_positive_num(self):
        expected = self.temp.getter_id(52772)
        self.assertEqual(len(expected), 1)
    
    def test_get_meal_error_str(self):
        expected = self.temp.getter_id("421421421")
        self.assertEqual(expected, "Invalid ID")
    
    def test_get_meal_error_num(self):
        expected = self.temp.getter_id(32131321)
        self.assertEqual(expected, "Invalid ID")

if __name__ == '__main__':
    unittest.main()
