import unittest
from datetime import datetime
from typing import Any


def convert_date_format(date_str: str) -> str:
    """
    Convert a date from "YYYY-MM-DD" to "DD-MM-YYYY".
    Raises ValueError for non-string or invalid/incorrect formats.
    """
    if not isinstance(date_str, str):
        raise ValueError("date must be a string in YYYY-MM-DD format")
    s = date_str.strip()
    if not s:
        raise ValueError("empty date string")
    try:
        dt = datetime.strptime(s, "%Y-%m-%d")
    except Exception as exc:
        raise ValueError("invalid date or format, expected YYYY-MM-DD") from exc
    return dt.strftime("%d-%m-%Y")


class TestConvertDateFormat(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_leap_year_valid(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")

    def test_non_leap_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("2019-02-29")

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-01")

    def test_invalid_day(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")

    def test_whitespace_ok(self):
        self.assertEqual(convert_date_format(" 2023-01-05 "), "05-01-2023")

    def test_wrong_separator(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/01/05")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_none_input(self):
        with self.assertRaises(ValueError):
            convert_date_format(None)  # type: ignore

    def test_numeric_input(self):
        with self.assertRaises(ValueError):
            convert_date_format(20231015)  # type: ignore

    def test_already_dd_mm_yyyy(self):
        # Input already in DD-MM-YYYY should be rejected (expects YYYY-MM-DD)
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        print("Convert YYYY-MM-DD -> DD-MM-YYYY (type Enter to exit)")
        while True:
            try:
                raw = input("Enter date (YYYY-MM-DD): ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not raw:
                break
            try:
                out = convert_date_format(raw)
                print("Converted:", out)
            except ValueError as e:
                print("Error:", e)
