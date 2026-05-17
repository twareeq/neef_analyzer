import cleaner
import filters
import reports

# Load and clean
raw = cleaner.open_file("dirty_transactions.csv")
cleaned = cleaner.clean_data(raw)
# cleaner.export_data(cleaned_data)

# Load reference data
agents_data = filters.open_csv("data/agents.csv")
bank_data = filters.open_csv("data/bank_codes.csv")
transactions = filters.read_file("data/transactions.csv")

# Filter
filtered_data = filters.filter_combined(transactions, agents_data, bank_data)

# Report
reports.generate_report(filtered_data)

# Export
cleaner.export_data(filtered_data, "filtered_results")
