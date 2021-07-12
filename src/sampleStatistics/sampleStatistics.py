from generalStatistics.generalStatistics import GeneralStatistics


class SampleStatistics(GeneralStatistics):
    result = 0

    def __init__(self):
        super().__init__()
        pass

    def s_var(self, a):
        b = self.diff_sqr_sum(a)
        self.result = self.div(b, len(a)-1)
        return self.result

    def s_std_dev(self, a):
        self.result = (self.sqroot(self.s_var(a)))
        return self.result
