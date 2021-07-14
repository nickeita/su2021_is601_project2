from generalStatistics.generalStatistics import GeneralStatistics
from sampleStatistics.sampleVariance import sample_variance
from sampleStatistics.sampleStandardDeviation import sample_std_deviation


class SampleStatistics(GeneralStatistics):
    result = 0

    def __init__(self):
        super().__init__()
        pass

    def s_var(self, a):
        self.result = sample_variance(a)
        return self.result

    def s_std_dev(self, a):
        self.result = sample_std_deviation(a)
        return self.result
