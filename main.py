import cleaner
import filters
import reports

# Load and clean
raw = cleaner.open_file("data/neef/fdh_statement.xlsx")
cleaned = cleaner.clean_data(raw)
cleaner.export_data(cleaned, "clean_transactions")

# Load reference data
agents_data = filters.open_csv("data/agents.csv")
bank_data = filters.open_csv("data/bank_codes.csv")

transactions = cleaner.open_file("data/clean_data/clean_transactions.xlsx")

# Filter
ref_list = ["FDH", "MZM", "RPY"]
agent_codes = agents_data
description = ["Cash Deposit", "Online Banking Transfer"]
filtered_data = filters.filter_combined(transactions, description, ref_list, agents_data)

# Report
reports.generate_report(filtered_data)

# Export
cleaner.export_data(filtered_data, "filtered_transactions")
