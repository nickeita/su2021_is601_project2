import unittest
from generalStatistics.generalStatistics import GeneralStatistics
from randomData.randomData import RandomData
from statistics import mean, median, mode

g_data = RandomData()
g_size = g_data.r_size(15, 30)
g_list = g_data.r_pop(50, 95, g_size)
elements = g_data.r_data(g_list, int(0.5 * g_size))


class GeneralStatisticsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.g_stats = GeneralStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.g_stats, GeneralStatistics)
        
    def test_general_mean_method(self):
        self.assertEqual(self.g_stats.g_mean(elements), mean(elements))
    
    def test_general_median_method(self):
        self.assertEqual(self.g_stats.g_median(g_list), median(g_list))

    def test_general_mode_method(self):
        self.assertEqual(self.g_stats.g_mode(g_list), mode(g_list))


if __name__ == '__main__':
    unittest.main()
