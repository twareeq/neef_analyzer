# report.py — contains generate_report that takes the filtered DataFrame and prints total transactions, 
# total credit amount, total debit amount, and lists each transaction cleanly.

def generate_report(data):
    total_ts = len(data)
    total_credits = data['credit'].sum()
    total_debits = data['debit'].sum()

    print(f"Total transactions: {total_ts}")
    print(f"Total Credited Amount: {total_credits:,.2F}")
    print(f"Total Debited Amount: {total_debits:,.2F}")

    print("ALL TRANSACTIONS")
    for _, row in data.iterrows():
        print(f"{row['bookingDate']}, {row['details']}, MWK {row['credit']:,.2F}")
