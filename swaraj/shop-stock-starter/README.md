# Local stock planner — provisional starter

This is an editable **example**, not a completed fieldwork submission. The topic is a small shop deciding what quantity to reorder. Use it only if your own recent, nearby observation and conversation support it; otherwise adapt the tool to the problem you actually found.

## What it does

For each item, it suggests `max(0, daily_sales × (lead_days + 1) − stock)`. The extra day is a provisional buffer. Confirm the rule and units with the person. The output is a planning suggestion, not an automatic purchase order.

## Data you must collect

Visit the place yourself and collect **at least 20 real entries**. Put them in `data.csv` using the columns below. One row means one distinct item; if you cannot collect 20 real items, change the data model to fit your observations instead of inventing entries.

| Column | Meaning |
| --- | --- |
| `item` | Unique item name |
| `stock` | Current units on hand, whole number |
| `daily_sales` | Units sold in a day, whole number; record how you determined it |
| `lead_days` | Whole days until a new order arrives |

The supplied `data.csv` contains only a header. It has no observations.

## Run and test

Requires Python 3.9+ and no extra packages. In this folder:

```bash
python stock_planner.py data.csv
python -m unittest discover -s tests
```

The program rejects missing files, missing columns, duplicate item names, negative or non-integer values, and malformed rows. It reports row numbers and exits without giving a plan if any row is invalid. Before real data is entered, it reports that no data rows were found.

## Real result and limitations — complete after fieldwork

- Place, person, date: [your actual details]
- Command run and **real output**: [paste output from your own populated CSV]
- What this gets wrong for this person: [specific issues you observed]
- 3-minute screen recording link: [link after recording]

The current rule assumes steady sales and known delivery time. It ignores weekends, promotions, spoilage, storage limits, and pack sizes. Ask the person which of these matter and revise the rule accordingly.

## 24-hour submission checklist

- [ ] In the **first hour**, finish `research.md` with your observed problem and named person, then make your **first commit** containing it. This starter cannot backdate that event.
- [ ] Spend 20 minutes at the place, take two actual timestamped photos, talk to the person, and complete `fieldwork.md`.
- [ ] Collect 20+ real entries in `data.csv`; run the program, fix any invalid rows, and document the real output above.
- [ ] Write your own half-page `reflection.md` without AI.
- [ ] Record a 3-minute demonstration and link it above.
- [ ] Export actual AI chats into `ai-chats/`.
- [ ] Make at least five genuine commits **spread across the day**, using your own commit messages. Do not manufacture dates or history.
- [ ] Push to a public Git repository and email the link within 24 hours of starting.
- [ ] Be ready to explain one CSV row, feed in a bad row, and change a threshold live in the follow-up call.

No commits, public repository, photos, chat exports, real observations, recording, or email submission are claimed by this starter.
