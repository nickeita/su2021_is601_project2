import unittest
from sampleStatistics import SampleStatistics


class SampleStatisticsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s_stats = SampleStatistics()

    def test_object_instance(self):
        self.assertIsInstance(self.s_stats, SampleStatistics)


if __name__ == '__main__':
    unittest.main()