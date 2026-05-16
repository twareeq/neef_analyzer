## Day 13 — Saturday Build Day. NEEF Statement Analyzer

> This is my Week 2 capstone. neef_analyzer files: main.py, cleaner.py, filters.py, report.py, and your CSV files.

Here's what the system must do end to end:

> cleaner.py — reads the raw CSV, cleans missing values, standardizes casing, strips whitespace, returns a clean DataFrame.
>
> filters.py — contains three functions: filter_by_reference that takes a DataFrame and a code like FDH and returns matching rows, filter_by_agent that takes a DataFrame and agent codes list and returns matching rows, and filter_combined that applies both filters together.
>
> report.py — contains generate_report that takes the filtered DataFrame and prints total transactions, total credit amount, total debit amount, and lists each transaction cleanly.
>
> main.py — ties everything together: load → clean → filter → report → export to CSV.

*This is the first version of a real tool I will actually use at work. Build it like it matters.*
