import unittest

class Calculator:

    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_negative_add(self):
        result = self.calc.add(2, -3)
        self.assertEqual(result, -1)

    def test_sub(self):
        result = self.calc.subtract(2, 3)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
