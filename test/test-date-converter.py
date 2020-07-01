import unittest
from src.date_converter import convert2unix, parse_date

class TestDateConverter(unittest.TestCase):
    def test_parse_date_v1(self):
        dt_parse_list = parse_date("05/25/2020 00:00:00")
        self.assertEqual(dt_parse_list, [5, 25, 2020, 0, 0, 0])

    def test_parse_date_v2(self):
        dt_parse_list = parse_date("06/18/2020 00:00:00")
        self.assertEqual(dt_parse_list, [6, 18, 2020, 0, 0, 0])

    def test_convert2unix(self):
        unix_timestamp = convert2unix("05/25/2020 00:00:00")
        self.assertEqual(unix_timestamp, 1590364800)

if __name__ == "__main__":
    unittest.main()