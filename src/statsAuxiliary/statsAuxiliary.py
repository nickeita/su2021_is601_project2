from calculator.calculator import Calculator
from statsAuxiliary.aggregate import aggregate
from statsAuxiliary.varianceInput import variance_input


class StatsAuxiliary(Calculator):
    result = 0

    def __init__(self):
        super().__init__()
        pass

    def aggr(self, a):
        self.result = aggregate(a)
        return self.result

    def var_input(self, a):
        self.result = variance_input(a)
        return self.result
