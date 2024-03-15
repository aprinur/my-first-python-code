# import library
import pandas as pd

print('Membuat DataFrame dari dict')
# Initialize data off lists
data = {'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output
print(df)

print('\n Membuat DataFrame dari List')

# Membuat List yang berisi string
daftar = ['Oleh', 'Karena', 'Itu', 'Penjajahan', 'Diatas', 'Dunia', 'Harus', 'Dihapuskan']

# Memanggil DataFrame constructor pada list
dr = pd.DataFrame(daftar)

# Mencetak DataFrame
print(dr)

print('\n Membuat DataFrame kosong')

# Calling DataFrame constructor
dt = pd.DataFrame()

# Mencetak DataFrame
print(dt)

