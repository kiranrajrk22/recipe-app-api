from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(3, 4)
        self.assertEqual(res, 7)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(5, 10)
        self.assertEqual(res, 5)