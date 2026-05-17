import csv

def open_csv(data):
    with open(data) as row:
        return list(csv.DictReader(row))

def filter_by_reference(statement, code_list):
    codes = tuple(code for code in code_list)
    pattern = "|".join(codes)

    return statement[statement['Reference'].str.contains(pattern, na=False)]

def filter_by_description(statement, desc):
    des = tuple(d for d in desc)
    des_pattern = "|".join()
    return statement[statement['Description'].str.contains(des_pattern)]

def filter_by_agent(statement, agent_list):
    codes = tuple(agent['agentCode'] for agent in agent_list)
    pattern = "|".join(codes)

    return statement[statement["Payment details"].str.contains(pattern, na=False)]

def filter_combined(statement, desc, ref_code, agent_list):
    ref = tuple(code for code in ref_code)
    a_codes = tuple(agent['agentCode'] for agent in agent_list)
    des = tuple(d for d in desc)


    ref_pattern = "|".join(ref)
    agent_pattern = "|".join(a_codes)
    des_pattern = "|".join(des)

    return statement[
        statement['Description'].str.contains(des_pattern) |
        statement['Reference'].str.contains(ref_pattern) |
        statement['Payment details'].str.contains(agent_pattern)
    ]
