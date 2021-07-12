import unittest
from populationStatistics.populationStatistics import PopulationStatistics
from randomData.randomData import RandomData
from statistics import pvariance, pstdev, mean

p_data = RandomData()
p_size = p_data.r_size(25, 50)
p_list = p_data.r_pop(30, 95, p_size)


class PopulationStatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.p_stats = PopulationStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.p_stats, PopulationStatistics)

    def test_population_variance_method(self):
        self.assertAlmostEqual(self.p_stats.p_var(p_list), pvariance(p_list))

    def test_population_standard_deviation(self):
        self.assertAlmostEqual(self.p_stats.p_std_dev(p_list), pstdev(p_list))


if __name__ == '__main__':
    unittest.main()
