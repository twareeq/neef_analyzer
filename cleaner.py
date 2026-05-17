# cleaner.py — reads the raw CSV, cleans missing values, standardizes casing, strips whitespace, returns a clean DataFrame.

import pandas as pd

def open_file(file_name):
    return pd.read_csv(f"data/{file_name}")

def clean_data(data):
    data.fillna({"debit": 0, "credit": 0}, inplace=True)
    data.fillna({"description": "Unknown"}, inplace=True)
    data["balance"] = data["balance"].ffill()
    data["details"] = data["details"].str.strip()
    data["description"] = data["description"].str.title()
    return data

def export_data(data, name):
    data.to_csv(f"data/clean_data/{name}.csv", index=False)
    print("Data exported successfully..")
