import unittest
from generalStatistics import GeneralStatistics


class GeneralStatisticsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.g_stats = GeneralStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.g_stats, GeneralStatistics)


if __name__ == '__main__':
    unittest.main()
