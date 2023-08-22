import unittest

def sum(a, b):
    return a+b

class test_sum(unittest.TestCase):

    def test_sum(self):

        res = sum(2, 3)

        self.assertEqual(res, 5)

    def test_zero(self):

        res = sum(0, 0)

        self.assertEqual(res, 0)

    def test_single_zero(self):

        res = sum(1, 0)

        self.assertEqual(res, 1)

    def test_negative(self):

        res = sum(2, -4)

        self.assertEqual(res, -2)

if __name__ == "__main__":
    unittest.main()