# Contains three functions: filter_by_reference that takes a DataFrame and a code like FDH and returns matching rows, 
# filter_by_agent that takes a DataFrame and agent codes list and returns matching rows, 
# and filter_combined that applies both filters together.
import pandas as pd
import csv

def read_file(filename):
    return pd.read_csv(filename)

def open_csv(filename):
    with open(filename) as row:
        return list(csv.DictReader(row))

def filter_by_reference(statement, bank_code):
    codes = tuple(code['bankCode'] for code in bank_code)
    pattern = "|".join(codes)
    return statement[statement['reference'].str.contains(pattern, na=False)]

def filter_by_agent(statement, agents_code):
    codes = tuple(code['agentCode'] for code in agents_code)
    pattern = "|".join(codes)
    return statement[statement['details'].str.contains(pattern, na=False)]

def filter_combined(statement, agents_code, bank_code):
    a_codes = tuple(code['agentCode'] for code in agents_code)
    b_codes = tuple(code['bankCode'] for code in bank_code)

    a_pattern = "|".join(a_codes)
    b_pattern = "|".join(b_codes)

    return statement[
    statement['details'].str.contains(a_pattern, na=False) & 
    statement['reference'].str.contains(b_pattern, na=False)
    ]
