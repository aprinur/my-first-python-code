import pandas as pd
import numpy as np
# Penggunaan fillna()
kamus = {'First Score': [100, 90,  np.nan, 95],
         'Second Score': [30, 45, 50, np.nan],
         'Third Score': [np.nan, 40, 80, 99]}

df = pd.DataFrame(kamus)

# Filling the missing value using fillna()
df.fillna(0)
print('Sebelum menggunakan fungsi fillna()\n')
print(df)
print('\nSetelah menggunakan fillna()\n')
print(df.fillna(0))

# Penggunaan replace()

kamus2 = {
    "Array_1": [49.50, 70],
    "Array_2": [65.1, 49.50]
}

data = pd.DataFrame(kamus2)

print(f'\n Sebelum penggunaan replace()\n')
print(data)
print('\n Setelah penggunaan replace() dengan nilai 49.5 diubah menjadi 60\n')
print(data.replace(49.50, 60))
