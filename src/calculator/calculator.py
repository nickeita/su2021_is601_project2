class Calculator:
    def __init__(self):
        pass

    # a plus b
    @staticmethod
    def add(a, b):
        return a + b

    # b minus a
    @staticmethod
    def sub(a, b):
        return b - a

    # a multiply by b
    @staticmethod
    def mul(a, b):
        return a * b

    # a divided by b
    @staticmethod
    def div(a, b):
        try:
            return b / a
        except ArithmeticError:
            print('Not Found')

    # a raised to the power of n
    @staticmethod
    def npow(a, n):
        try:
            return a ** n
        except ArithmeticError:
            print('Not Found')

    def sum(self):
        pass

    def prod(self):
        pass