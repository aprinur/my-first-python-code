# *args
"""
  Dalam *args yang dibutuhkan adalah tanda '*' karakter string dibelakangnya bisa diubah
  sesuai kebutuhan. contoh *data, *angka, dsb
"""


# * memasukkan banyak data ke dalam fungsi tanpa *args

# memasukkan banyak argumen
def fungsi(nama, tinggi, berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi('ucup', 170, 49)


# memasukkan argumen berbentuk list
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi(['otong', 140, 40])
# agar banyak data bisa dimasukkan kedalam fungsi yang memiliki satu parameter maka perlu
# dijadikan list dengan cara menambahkan kurung siku pada data yang akan dimasukkan.


# * memasukkan data/ argumen ke dalam fungsi dengan *args

def fungsi(*args):
    # parameter *args digunakan agar dapat memasukkan banyak data kedalam fungsi yang hanya memiliki satu parameter
    # tanpa perlu mengubahnya menjadi list.
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi('dudung', 167, 54)


# contoh lain penggunaan *args
def tambah(*data):  # kata args bisa diganti sesuai kebutuhan
    output = 0
    for angka in data:
        output += angka

    return output


hasil = tambah(4, 2, 6, 8, 4, 6, 23, 9)
print(hasil)
print(tambah(4382, 7523498, 19350, 89347))

'''
    *args berfungsi untuk memasukkan data kedalam fungsi namun belum diketahui banyaknya data
    yang akan dimasukkan
'''