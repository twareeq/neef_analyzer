# Contains three functions: filter_by_reference that takes a DataFrame and a code like FDH and returns matching rows, 
# filter_by_agent that takes a DataFrame and agent codes list and returns matching rows, 
# and filter_combined that applies both filters together.
import csv

def open_file(file_name):
    with open(f"data/{file_name}") as file:
        data = csv.DictReader(file)
        return list(data)

def filter_by_reference(statement, bank_codes):
    codes = tuple(code['bankCode'] for code in bank_codes)
    return [t for t in statement if t['reference'].endswith(codes)]

def filter_by_agent(statement, agents_code):
    codes = tuple(code['agentCode'] for code in agents_code)
    return [t for t in statement if any(code in t['details'] for code in codes)]

def filter_combined(statement, agents_code, bank_code):
    agent = tuple(code['agentCode'] for code in agents_code)
    bcode = tuple(code['bankCode'] for code in bank_code)

    return [t for t in statement if any(code in t['details'] for code in agent) or t['reference'].endswith(bcode)]

def print_row(statement):
    for t in statement:
        print(t)
    
data = open_file("transactions.csv")
agents_data = open_file("agents.csv")
bank_data = open_file("bank_codes.csv")

print_row(filter_combined(data, agents_data, bank_data))
