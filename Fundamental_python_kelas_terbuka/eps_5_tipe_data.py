# tipe data adalah berbagai macam data yang bisa dimasukkan kedalam variabel

# tipe data : angka satuan ( integer/ int)
data_integer = 5  # angka 1 hanya contoh bisa diganti bilangan bulat lainnya
print(" data: ", data_integer, ", bertipe : ", type(data_integer))

# tipe data : angka dengan koma atau desimal (float)
data_float = 1.5  # angka 1.5 hanya contoh bisa diganti bilangan desimal lainnya
print(" data: ", data_float, ", bertipe : ", type(data_float))

# tipe data : kumpulan karakter ( string )
data_string = 'ucup'  # ucup hanya contoh bisa diganti karakter lainnya
print(" data: ", data_string, ", bertipe : ", type(data_string))

# tipe data : biner true/false ( boolean )
data_bool = True  # true bisa diganti dengan false
print(" data: ", data_bool, ", bertipe : ", type(data_bool))


"""tipe data khusus"""

# bilangan kompleks
data_complex = complex(5, 6)
print(" data: ", data_complex, ", bertipe : ", type(data_complex))
# saat dijalankan akan ada huruf j menjadi (5+6j), huruf j adalah imajiner

# tipe data dari bahasa C
from ctypes import c_double  # cara memanggil fungsi

data_c_double = c_double(10.5)
print(" data: ", data_c_double, ", bertipe : ", type(data_c_double))
