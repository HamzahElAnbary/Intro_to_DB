import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test addition with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction with various cases."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(3, -2), 5)

    def test_multiply(self):
        """Test multiplication including edge cases."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test division including divide by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
