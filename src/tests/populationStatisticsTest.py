import unittest
from populationStatistics.populationStatistics import PopulationStatistics


class PopulationStatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.p_stats = PopulationStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.p_stats, PopulationStatistics)


if __name__ == '__main__':
    unittest.main()
