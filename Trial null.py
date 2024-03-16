# Import pandas
import pandas as pd

# Import numpy
import numpy as np

# Data dict
daftar = {'First Score': [100, 90, np.nan, 95],
          'Second Score': [30, 45, 56, np.nan],
          'Third Score': [np.nan, 40, 80, 98]}

# Membuat dataframe
df = pd.DataFrame(daftar)

print('\n\nPenggunaan .isnull()\n')
# Menggunakan isnull()
newdf = df.isnull()

# Mencetak data
print(newdf.to_string())

print('\n\n Penggunaan .notnull()')
# Menggunakan notnull()
newdf2 = df.notnull()

# Mencetak data
print('\n', newdf2.to_string())
