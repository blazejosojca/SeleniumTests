from unittest import TestCase
from . import calculate

class TestCalculator(TestCase):
    # calculate_percent(1, 2)
    # calculate_percent('1', 2)
    # calculate_percent('a', None)
    # calculate_percent(28, 0)
    # calculate_percent(50, 99)

    def test_upper(self):
        result = calculate.cacalculate_percent(1,2)
        self.assertEqual(result, 0.5)