import unittest
from calculator.calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_object_instance(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition_method(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_subtraction_method(self):
        self.assertEqual(self.calc.sub(3, 1), 2)

    def test_multiplication_method(self):
        self.assertEqual(self.calc.mul(1, 2), 2)

    def test_division_method(self):
        self.assertAlmostEqual(self.calc.div(4, 2), 2.00000000)

    def test_power_method(self):
        self.assertEqual(self.calc.npow(2, 2), 4)

    def test_root_method(self):
        self.assertEqual(self.calc.nroot(4, 2), 2)


if __name__ == '__main__':
    unittest.main()
