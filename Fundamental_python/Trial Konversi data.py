import pandas as pd

# Membuat Series dengan type data integer

data = [1, 2, 3, 4, 5, 6]
series = pd.Series(data)

# Mengubah tipe data Series menjadi tipe data string


series_string = series.astype(str)
print(series_string)
print('\n')

# Mengubah tipe data Series menjadi list dengan .tolist()

series_string2 = series.tolist()
print('Hasil dari Series menjadi List')
print(series_string2)
print('\n')

# Mengubah tipe data Series menjadi dict dengan to_dict()

series_string3 = series.to_dict()
print('Hasil dari series menjadi Dict')
print(series_string3)
print('\n')
