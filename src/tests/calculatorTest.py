import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_object_instance(self):
        self.assertIsInstance(self.calc, Calculator)


if __name__ == '__main__':
    unittest.main()
