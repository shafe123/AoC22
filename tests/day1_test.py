import unittest
import day1

class TestMethods(unittest.TestCase):
    example_set = [1000, 2000, 3000, None, 4000, None, 5000, 6000, None, 7000, 8000, 9000, None, 10000]

    def test_count_calories(self):
        self.assertEqual(day1.count_calories([1, 2, 3, None, 4, 5, 6]), [6, 15])

    def test_sum_calories(self):
        self.assertEqual(day1.part_one(True), 24000)

    def test_top_three(self):
        self.assertEqual(day1.part_two(True), 45000)