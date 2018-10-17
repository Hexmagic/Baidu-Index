import unittest
from channel.baidu import Trend


class TestTrend(unittest.TestCase):
    def setUp(self):
        self.trend = Trend(word="btc", date="2018-09-09", number=123)

    def test_trend(self):
        print(self.trend)


if __name__ == '__main__':
    unittest.main()
