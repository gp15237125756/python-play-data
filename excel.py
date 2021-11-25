import pandas as pd


def assignment():
    # openpyxl引擎支持xlsx
    pe = pd.read_excel('scores.xlsx', engine='openpyxl', sheet_name=0)
    print(pe)
    pe['sum'] = pe['Python'] + pe['Math']
    pe.to_excel('students.xlsx')


if __name__ == "__main__":
    assignment()
