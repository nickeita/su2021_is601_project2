import unittest
from sampleStatistics.sampleStatistics import SampleStatistics
from randomData.randomData import RandomData
from statistics import variance, stdev

s_data = RandomData()
s_size = s_data.r_size(25, 50)
s_list = s_data.r_pop(30, 95, s_size)


class SampleStatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s_stats = SampleStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.s_stats, SampleStatistics)

    def test_sample_variance_method(self):
        self.assertAlmostEqual(self.s_stats.s_var(s_list), variance(s_list))

    def test_population_standard_deviation(self):
        self.assertAlmostEqual(self.s_stats.s_std_dev(s_list), stdev(s_list))


if __name__ == '__main__':
    unittest.main()
