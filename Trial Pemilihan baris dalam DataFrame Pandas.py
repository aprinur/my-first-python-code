import pandas as pd

# Membuat DataFrame dari file csv
nba = pd.read_csv('nba.csv', index_col='Name')

print('Mengambil baris dengan metode .loc[]')
# Mengamil baris dengan metode .loc[]

first = nba.loc['Avery Bradley']
second = nba.loc['R.J. Hunter']

print(first, '\n\n\n', second)

print('\n\n\n Mengambil baris dengan metode .iloc[] \n')

data = nba.iloc[5]

print(data)
