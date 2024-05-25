import pandas as pd
# Iterasi pada baris
""" fungsi iterrow() digunakan untuk mendapatkan setiap elemen baris dataframe """

kamus = {'name': ["Leo", "Fabio", "Rey", "Matt"],
         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
         'score': [90, 40, 80, 98]}

df = pd.DataFrame(kamus)

# Hasil iterasi pada baris
print('\nHasil iterasi baris\n')
for column, row in df.iterrows():
    print(column, row)
    print()

# Iterasi pada kolom

kamus2 = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
          'degree': ["MBA", "BCA", "M.Tech", "MBA"],
          'score': [90, 40, 80, 98]}

dd = pd.DataFrame(kamus2)

print('\n\nDataframe yang akan dilakukan iterasi\n')
print(dd)

# Hasil iterasi pada kolom

print('\nHasil iterasi kolom\n')
columns = list(dd)
for i in columns:
    print(dd[i][2])
