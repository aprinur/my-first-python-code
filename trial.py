import pandas as pd

series_from_excel = pd.read_excel('Book2.xlsx')
print(series_from_excel.to_string())
