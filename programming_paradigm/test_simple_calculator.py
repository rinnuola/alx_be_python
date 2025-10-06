import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for addition ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    # --- Tests for subtraction ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    # --- Tests for multiplication ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- Tests for division ---
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
