
# * Global scope variabe
""" Adalah variabel yang bisa dipanggil dimana saja didalam kode """

nama_global = 'otong'  # <-- disebut variabel global


# mengakses variabel global dalam fungsi
def fungsi1():
    print(f'fungsi menampilkan {nama_global}')


fungsi1()

# mengakses variabel global dalam loop

for i in range(0, 5):
    print(f'loop {i} - {nama_global}')

# mengakses variabel global dalam percabangan

if True:
    print(f'if menampilkan {nama_global}')

# * Local scope variabel
"""
    Adalah variabel yang didefinisikan didalam fungsi yang hanya bisa diakses dan digunakan 
    didalam fungsi tersebut
"""


def fungsi2():
    nama_local = 'Ucup'  # <-- local scope variabel


fungsi2()
# print(nama_local) <-- Akan eror karena nama_local hanya bisa dipakai di dalam fungsi2


# * Contoh penggunaan

# 1. mengakses variabel

def say_otong():
    print(f'hello {nama}')


nama = 'Otong'
say_otong()

# 2. Merubah variabel global
angka = 0
name = 'Udcup'


def ubah(nilai_baru, nama_baru):
    global angka  # 'angka' merujuk ke global scope variable diluar fungsi
    global name
    """ keyword 'global' berfungsi sebagai penanda, apabila variabel dibelakangnya mengambil
     dari global scope, bukan membuat local variabel baru"""
    angka = nilai_baru
    name = nama_baru


print(f'sebelum {angka}, {name}')
ubah(13, 'Udjang')
print(f'sesudah {angka}, {name}')


# * variabel scope pada perulangan dan percabangan

# Perulangan
angka = 0

for i in range(0, 5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 20

print(angka)
print(angka_dummy)

""" Global dan local scope hanya berlaku pada fungsi"""