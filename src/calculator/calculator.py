from calculator.addition import addition
from calculator.subtraction import subtraction
from calculator.multiplication import multiplication
from calculator.division import division
from calculator.nthPower import nth_power
from calculator.nthRoot import nth_root
from calculator.aggregate import aggregate
from calculator.nSquared import n_squared
from calculator.squareRoot import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def mul(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqr(self, a):
        self.result = n_squared(a)
        return self.result

    def sqroot(self, a):
        self.result = square_root(a)
        return self.result

    def npow(self, a, n):
        self.result = nth_power(a, n)
        return self.result

    def nroot(self, a, n):
        self.result = nth_root(a, n)
        return self.result

    def aggr(self, a):
        self.result = aggregate(a)
        return self.result
