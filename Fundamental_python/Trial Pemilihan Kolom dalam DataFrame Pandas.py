# Mengimpor Library
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Leo', 'Rey', 'Bob', 'Lucy'],
        'Age': [23, 22, 25, 24],
        'Address': ['London', 'Paris', 'Bali', 'Baghdad'],
        'Qualification': ['MSC', 'MS', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print('Menampilkan nama_global dan Kualifikasi \n')
# Select two columns
print(df[['Name', 'Qualification']])

alamat = data['Address']
print('\n\nMenampilkan alamat dari list\n')
print(alamat, '\n\n')

# Import csv file
nba = pd.read_csv('../nba.csv', index_col='Name')

# Retrieving column by indexing operator
first = nba['Age']
second = nba['Team']

print('\n Menampilkan kolom berdasarkan index operator\n')
print(first, '\n\n', second)
