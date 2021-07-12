from generalStatistics.generalStatistics import GeneralStatistics


class PopulationStatistics(GeneralStatistics):
    result = 0
    
    def __init__(self):
        super().__init__()
        pass

    def p_var(self, a):
        b = self.diff_sqr_sum(a)
        self.result = self.div(b, len(a))
        return self.result

    def p_std_dev(self, a):
        self.result = self.sqroot(self.p_var(a))
        return self.result

