"""Casting tipe data adalah merubah suatu tipe data ke tipe data lainnya"""

# tipe data : int, float, str, boolean(bool)


# INTEGER
print('\nMengubah data integer')
data_int = 9
print("data = ", data_int, " type = ", type(data_int))

# Mengubah data dari integer ke float
data_float = float(data_int)
print("data = ", data_float, " type = ", type(data_float))

# Mengubah data dari integer ke string
data_str = str(data_int)
print("data = ", data_str, " type = ", type(data_str))

# Mengubah data dari integer ke boolean
data_bool = bool(data_int)  # Hasil akan false apabila nilai nol
print("data = ", data_bool, " type = ", type(data_bool))


# FLOAT
print('\n\nMengubah data float ')

data_float = 9.5
print("data = ", data_float, " type = ", type(data_float))

# Mengubah data dari float ke integer
data_integer = int(data_float)  # Hasil akan dibulatkan kebawah/ angka dibelakang koma dihilangkan
print("data = ", data_integer, " type = ", type(data_integer))

# Mengubah data dari float ke string
data_str = str(data_float)
print("data = ", data_str, " type = ", type(data_str))

# Mengubah data dari float ke boolean
data_bool = bool(data_float)  # Hasil akan false apabila nilai nol
print("data = ", data_bool, " type = ", type(data_bool))


# BOOLEAN
print('\n\nMengubah data Boolean ')

data_bool = False
print("data = ", data_bool, " type = ", type(data_bool))

# Mengubah data dari boolean ke integer
data_integer = int(data_bool)
print("data = ", data_integer, " type = ", type(data_integer))

# Mengubah data dari boolean ke string
data_str = str(data_bool)  # Hasil akan false apabila nilai False
print("data = ", data_str, " type = ", type(data_str))

# Mengubah data dari boolean ke float
data_float = float(data_bool)
print("data = ", data_float, " type = ", type(data_float))


# STRING
print('\n\nMengubah data STRING ')

data_bool = '12'
print("data = ", data_bool, " type = ", type(data_bool))

# Mengubah data dari string ke integer
data_integer = int(data_bool)
print("data = ", data_integer, " type = ", type(data_integer))
""" agar bisa diubah ke integer, string harus angka """

# Mengubah data dari string ke float
data_float = float(data_bool)  # Hasil akan false apabila nilai nol
print("data = ", data_float, " type = ", type(data_float))
""" agar bisa diubah ke float, string harus angka """

# Mengubah data dari string ke boolean
data_bool = bool(data_bool)
print("data = ", data_bool, " type = ", type(data_bool))
""" Boolean akan selalu true selama memiliki nilai, meskipun karakter stringnya adalah "0" 
    ataupun kata "False" """

