import unittest
from math import *
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_object_instance(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition_method(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_subtraction_method(self):
        self.assertEqual(self.calc.sub(1, 3), 2)

    def test_multiplication_method(self):
        self.assertEqual(self.calc.mul(1, 2), 2)

    def test_division_method(self):
        self.assertAlmostEqual(self.calc.div(2, 4), 2.00000000)

    def test_power_method_root(self):
        self.assertEqual(self.calc.npow(4, 0.5), 2)

    def test_power_method_integer(self):
        self.assertEqual(self.calc.npow(2, 2), 4)

    def test_power_method_mixed(self):
        self.assertEqual(self.calc.npow(4, 1.5), 8)


if __name__ == '__main__':
    unittest.main()
