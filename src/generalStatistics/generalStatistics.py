from statsAuxiliary.statsAuxiliary import StatsAuxiliary
from generalStatistics.generalMedian import general_median
from generalStatistics.generalMode import general_mode
from generalStatistics.generalMean import general_mean


class GeneralStatistics(StatsAuxiliary):
    result = 0

    def __init__(self):
        super().__init__()
        pass

    def g_mean(self, a):
        self.result = general_mean(a)
        return self.result

    def g_median(self, a):
        self.result = general_median(a)
        return self.result

    def g_mode(self, a):
        self.result = general_mode(a)
        return self.result


