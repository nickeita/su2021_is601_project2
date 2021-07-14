from generalStatistics.generalStatistics import GeneralStatistics
from populationStatistics.populationVariance import population_variance
from populationStatistics.populationStandardDeviation import population_std_deviation


class PopulationStatistics(GeneralStatistics):
    result = 0
    
    def __init__(self):
        super().__init__()
        pass

    def p_var(self, a):
        self.result = population_variance(a)
        return self.result

    def p_std_dev(self, a):
        self.result = population_std_deviation(a)
        return self.result

