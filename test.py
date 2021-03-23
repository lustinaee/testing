import unittest

class TestCalc(unittest.TestCase):

    def add_test(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
