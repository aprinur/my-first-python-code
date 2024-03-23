import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob'],
        'Kota': ['New York', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)

# Mengubah string menjadi lowercase
df['nama_lower'] = df['Nama'].str.lower()
print(df)

# Contoh Penggunaan Timestamp
tanggal = pd.Timestamp('2024-03-20')
print(f'\n', tanggal)
