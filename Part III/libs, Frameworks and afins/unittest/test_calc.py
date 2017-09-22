import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_divide(self):
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # or, the same test in another shape
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
