import tempfile
import unittest
from pathlib import Path

from stock_planner import plan, read_rows


class StockPlannerTests(unittest.TestCase):
    def test_order_rule(self):
        self.assertEqual(plan({"stock": 3, "daily_sales": 4, "lead_days": 2}), 9)
        self.assertEqual(plan({"stock": 20, "daily_sales": 4, "lead_days": 2}), 0)

    def test_valid_and_bad_rows(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as folder:
            file = Path(folder) / "data.csv"
            file.write_text("item,stock,daily_sales,lead_days\nRice,3,4,2\nMilk,no,4,1\nRice,2,1,1\n", encoding="utf-8")
            rows, errors = read_rows(file)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(errors), 2)
        self.assertIn("row 3", errors[0])
        self.assertIn("row 4", errors[1])

    def test_missing_header(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as folder:
            file = Path(folder) / "data.csv"
            file.write_text("item,stock\nRice,3\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Missing columns"):
                read_rows(file)


if __name__ == "__main__":
    unittest.main()
