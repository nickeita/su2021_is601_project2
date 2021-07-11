from calculator.calculator import Calculator


class GeneralStatistics(Calculator):
    result = 0
    length = 1

    def __init__(self):
        super().__init__()
        pass

    def g_mean(self, a, b):
        self.length = len(a)
        self.result = sum(a)/self.length
        return self.result

    def g_median(self):
        pass

    def g_mode(self):
        pass
