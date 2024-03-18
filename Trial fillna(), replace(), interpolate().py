import pandas as pd
import numpy as np
# Penggunaan fillna()
""" fillna() adalah metode yang digunakan untuk mengisi nilai nilai yang hilang dalam dataframe atau serias dengan nilai
yang ditentukan"""
kamus = {'First Score': [100, 90,  np.nan, 95],
         'Second Score': [30, 45, 50, np.nan],
         'Third Score': [np.nan, 40, 80, 99]}

df = pd.DataFrame(kamus)

print('Sebelum menggunakan fungsi fillna()\n')
print(df)

print('\nSetelah menggunakan fillna()\n')
# Filling the missing value using fillna()
print(df.fillna(0))

# Penggunaan replace()
""" replace() adalah metode yang digunakan untuk menggantikan nilai nilai tertentu dalam sebuah dataframe atau series 
dengan nilai yang baru"""
kamus2 = {
    "Array_1": [49.50, 70],
    "Array_2": [65.1, 49.50]
}

data = pd.DataFrame(kamus2)

print(f'\n\n\nSebelum penggunaan replace()\n')
print(data)
print('\n Setelah penggunaan replace() dengan nilai 49.5 diubah menjadi 60\n')

# mengganti nilai dengan replace()
print(data.replace(49.50, 60))


# Penggunaan interpolate()
""" interpolate() adalah fungsi yang digunakan untuk mengisi nilai nilai yang hilang dalah dataframe atau series dengan 
nilai yang dihasilkan dari interpolasi antara nilai nilai yang ada"""
kamus3 = pd.DataFrame({"A": [12, 4, 5, None, 1],
                       "B": [None, 2, 64, 3, None],
                       "C": [20, 16, None, 3, 8],
                       "D": [14, 3, None, None, 6]})

print('\n\n\nSebelum penggunaan interpolate()\n')
print(kamus3)
print('\nSetelah penggunaan interpolate()\n')

# mengisi nilai yang kosong dengan metode interpolate()
print(kamus3.interpolate(method='linear', limit_direction='forward', limit=1))

# atau bisa juga menggunakan cara berikut
# x = kamus3.interpolate(methode='linear', limit_direction='forward', limit=1)
# print(x)
