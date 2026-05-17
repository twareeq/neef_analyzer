def generate_report(statement):
    total_ts = len(statement)
    total_credit = statement['Credit'].sum()
    total_debit = statement['Debit'].sum()

    print(f"Total transactions: {total_ts:,.2f}")
    print(f"Total credits: {total_credit:,.2f}")
    print(f"Total debits: {total_debit:,.2f}")

    print("All Transactions")
    for _, row in statement.iterrows():
        print(f"{row['Value date']} | {row['Payment details']} | {row['Credit']}")
