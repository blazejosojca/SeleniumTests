from unittest import TestCase
from . import calculate
import os


class TestCalculator(TestCase):
    # calculate_percent(1, 2)
    # calculate_percent('1', 2)
    # calculate_percent('a', None)
    # calculate_percent(28, 0)
    # calculate_percent(50, 99)

    def test_happy_path(self):
        result = calculate.calculate_percent(1, 2)
        self.assertEqual('1 from 2 is 50.0 %', result)

    def test_type_error(self):
        result = calculate.calculate_percent('1', 2)
        self.assertEqual('Inappropriate argument type.', result)


