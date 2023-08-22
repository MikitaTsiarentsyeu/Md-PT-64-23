class Calculator:

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod    
    def mult(a, b):
        return a*b
    
calc = Calculator()
calc.add(2, 3)

calc2 = Calculator()
calc2.add(2, 3)

def add(a, b):
    return a+b

Calculator.add(2, 3)

class TwoNumbersCalc:

    @staticmethod
    def add(a, b):
        return a+b
    
class ThreeNumberCalc(TwoNumbersCalc):

    @staticmethod
    def add(a, b, c):
        return TwoNumbersCalc.add(TwoNumbersCalc.add(a,b),c)

