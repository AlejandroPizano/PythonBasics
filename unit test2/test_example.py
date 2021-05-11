import unittest
import calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(calc.add(5, 10), 15)
        self.assertEqual(calc.add(2, 10), 12)
        self.assertEqual(calc.add(5, 1), 6)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(2, 10), -8)
        self.assertEqual(calc.subtract(5, 1), 4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.multiply(2, 10), 20)
        self.assertEqual(calc.multiply(5, 1), 5)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 10), .5)
        self.assertEqual(calc.divide(2, 10), .2)
        self.assertEqual(calc.divide(5, 5), 1)
        self.assertRaises(ValueError, calc.divide, 5, 0)
        # same as last method.
        with self.assertRaises(ValueError):
            calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
