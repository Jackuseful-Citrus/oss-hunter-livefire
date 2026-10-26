import unittest

from duration_utils import parse_duration


class ParseDuration(unittest.TestCase):
    def test_hours(self):
        self.assertEqual(parse_duration("1h"), 3600)

    def test_minutes(self):
        self.assertEqual(parse_duration("30m"), 1800)

    def test_seconds(self):
        self.assertEqual(parse_duration("45s"), 45)

    def test_weeks(self):
        self.assertEqual(parse_duration("1w"), 604800)

    def test_days(self):
        for text, expected in (("0d", 0), ("1d", 86400), ("2d", 172800)):
            with self.subTest(text=text):
                self.assertEqual(parse_duration(text), expected)

    def test_days_combined_with_other_units(self):
        self.assertEqual(parse_duration("2d4h"), 187200)
        self.assertEqual(parse_duration("1w2d3h4m5s"), 788645)

    def test_days_preserve_input_normalization(self):
        self.assertEqual(parse_duration(" 1D "), 86400)

    def test_malformed_days_raise(self):
        for text in ("d", "1d!", "1d 2h", "-1d", "1.5d"):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_duration(text)

    def test_combined(self):
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            parse_duration("")


if __name__ == "__main__":
    unittest.main()
