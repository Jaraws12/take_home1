"""Small-shop stock planner. Replace the provisional example with your observed need."""

import argparse
import csv
from pathlib import Path

REQUIRED = ("item", "stock", "daily_sales", "lead_days")


def read_rows(path: Path):
    """Return valid records and specific errors; never silently accept bad rows."""
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV is empty or has no header")
        missing = set(REQUIRED) - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing columns: " + ", ".join(sorted(missing)))
        records, errors, seen = [], [], set()
        for line, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                errors.append(f"row {line}: wrong number of columns")
                continue
            if not any((value or "").strip() for value in row.values()):
                continue
            item = row["item"].strip()
            if not item:
                errors.append(f"row {line}: item is blank")
                continue
            if item.casefold() in seen:
                errors.append(f"row {line}: duplicate item {item!r}")
                continue
            try:
                values = {key: int(row[key].strip()) for key in REQUIRED[1:]}
            except ValueError:
                errors.append(f"row {line}: stock, daily_sales and lead_days must be whole numbers")
                continue
            if any(value < 0 for value in values.values()):
                errors.append(f"row {line}: numbers cannot be negative")
                continue
            if values["lead_days"] > 365:
                errors.append(f"row {line}: lead_days exceeds 365; check the entry")
                continue
            seen.add(item.casefold())
            records.append({"item": item, **values})
    return records, errors


def plan(row):
    """Simple provisional rule: cover sales until delivery plus one buffer day."""
    target = row["daily_sales"] * (row["lead_days"] + 1)
    return max(0, target - row["stock"])


def main():
    parser = argparse.ArgumentParser(description="Suggest quantities to reorder")
    parser.add_argument("csv_file", nargs="?", type=Path, default=Path("data.csv"))
    args = parser.parse_args()
    try:
        rows, errors = read_rows(args.csv_file)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    for error in errors:
        print("Warning:", error)
    if errors:
        parser.exit(1, "Fix invalid rows before using the plan.\n")
    if not rows:
        parser.exit(1, "No data rows found. Add your own observations to data.csv.\n")
    print("Item | In stock | Daily sales | Lead days | Suggested order")
    print("-" * 67)
    for row in sorted(rows, key=lambda r: (-plan(r), r["item"].casefold())):
        print(f'{row["item"]} | {row["stock"]} | {row["daily_sales"]} | {row["lead_days"]} | {plan(row)}')
    print("\nRule: cover expected sales until delivery plus one buffer day. Verify with the shopkeeper.")


if __name__ == "__main__":
    main()
