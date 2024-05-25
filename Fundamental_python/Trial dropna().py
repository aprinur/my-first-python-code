import numpy as np
import pandas as pd

# Penggunaan dropna()
# dropna() digunakan untuk menghapus baris dan kolom yang memiliki nilai null dengan berbagai cara

kamus = {'First Score': [100, 90, np.nan, 95],
         'Second Score': [30, np.nan, 45, 56],
         'Third Score': [52, 40, 80, 98],
         'Fourth Score': [np.nan, np.nan, np.nan, 65]}

# Membuat dataframe dari dictionary
df = pd.DataFrame(kamus)

print('Sebelum penggunaan dropna()')
print(df)
print('\nSetelah menggunakan dropma\n')
# Penggunaan metode dropna()
print(df.dropna())
