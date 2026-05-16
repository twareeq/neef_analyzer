# cleaner.py — reads the raw CSV, cleans missing values, standardizes casing, strips whitespace, returns a clean DataFrame.

import pandas as pd

def open_file(file_name):
    return pd.read_csv(f"data/{file_name}.csv")

def clean_data(data):
    data.fillna({"debit": 0, "credit": 0}, inplace=True)
    data.fillna({"description": "Unknown"}, inplace=True)
    data["balance"] = data["balance"].ffill()
    data["details"] = data["details"].str.strip()
    data["description"] = data["description"].str.title()
    return data

def export_data(data):
    data.to_csv("data/cleaned_data.csv", index=False)
    print("Data exported successfully..")

data = open_file("dirty_transactions")
export_data(clean_data(data))