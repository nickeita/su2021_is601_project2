from calculator.calculator import Calculator
from generalStatistics.generalMedian import general_median
from generalStatistics.generalMode import general_mode


class GeneralStatistics(Calculator):
    result = 0
    # length = 1

    def __init__(self):
        super().__init__()
        pass

    def g_mean(self, a):
        # self.length = len(a)
        self.result = self.div(self.aggr(a), len(a))
        return self.result

    def g_median(self, a):
        self.result = general_median(a)
        return self.result

    def g_mode(self, a):
        self.result = general_mode(a)
        return self.result

    def diff_sqr_sum(self, a):
        b = []
        c = []
        for i in range(len(a)):
            b.append(self.sub(a[i], self.g_mean(a)))
            c.append(self.sqr(b[i]))
        self.result = self.aggr(c)
        return self.result

