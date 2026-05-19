# cleaner.py — reads the raw CSV, cleans missing values, standardizes casing, strips whitespace, returns a clean DataFrame.

import pandas as pd

def open_file(file_name):
    return pd.read_excel(file_name)

def clean_data(data):
    data.fillna({'Credit': 0}, inplace=True)
    data.fillna({'Debit': 0}, inplace=True)
    data['Balance'] = data['Balance'].ffill()
    data['Payment details'] = data['Payment details'].str.strip()
    return data

def export_data(data, name):
    data.to_excel(f"data/clean_data/{name}.xlsx", index=False)
    print("data exported successfully...")
