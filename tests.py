""" Unittests for pizzabot delivering"""
import unittest
from pizzabot import pizzabot


class TestUser(unittest.TestCase):

    def test_correct_data(self):
        result = pizzabot("5x5 (1, 3) (4, 4)")
        self.assertEqual(result, "ENNNDEEEND")

    def test_double_delivering(self):
        result = pizzabot("5x5 (0, 0) (1, 3) (4,4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)")
        self.assertTrue("DD" in result)

    def test_empty_data(self):
        self.assertRaises(ValueError, pizzabot, "")

    def test_wrong_area_value(self):
        self.assertRaises(ValueError, pizzabot, "5xx (1, 3) (4, 4)")

    def test_wrong_point_value(self):
        self.assertRaises(ValueError, pizzabot, "5x5 (1, #) (4, 4)")

    def test_broken_area(self):
        with self.assertRaises(ValueError) as context:
            pizzabot("55 (1, 3) (4, 4)")
        self.assertEqual("Area size hasn't been detected", str(context.exception))

    def test_broken_points(self):
        with self.assertRaises(ValueError) as context:
            pizzabot("5x5 ")
        self.assertEqual("No one delivery point has been found", str(context.exception))

    def test_out_of_area_range(self):
        with self.assertRaises(ValueError) as context:
            pizzabot("5x5 (1, 30) (4, 4)")
        self.assertTrue("point is out of area range." in str(context.exception))

    def test_negative_points(self):
        with self.assertRaises(ValueError) as context:
            pizzabot("5x5 (1, 30) (-4, 4)")
        self.assertTrue("point is out of area range." in str(context.exception))


if __name__ == '__main__':
    unittest.main()
