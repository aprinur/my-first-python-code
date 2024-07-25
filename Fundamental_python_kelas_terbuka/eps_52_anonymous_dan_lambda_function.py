# ** Lambda function
"""
    Lambda function berfungsi membuat program menjadi lebih sederhana

"""


# contoh fungsi tanpa lambda
def f_kuadrat(angka):
    return angka ** 2


print(f'Hasil fungsi kuadrat  = {f_kuadrat(3)}')

'''
    template lambda:
    
    output = lambda argument: expression
    
'''
# * contoh contoh penggunaan lambda

kuadrat = lambda angka: angka ** 2
print(f'hasil lambda kuadrat = {kuadrat(5)}')

pangkat = lambda ang, pang: ang ** pang  # ang dan pang menjadi parameter yang harus diisi
print(f'hasil lambda pangkat = {pangkat(5, 3)}')

pangkat = lambda ang=8, pang=2: ang ** pang  # parameter bisa diberi nilai default
print(f'hasil lambda pangkat = {pangkat()}')


# * sorting

data_list = ['Otong', 'Ucup', 'Dudung']

# sorting list berdasarkan abjad
data_list.sort()
print(f'sorted list = {data_list}')


# sorting list berdasarkan banyaknya huruf dalam kata dengan fungsi
def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(f'sorted list by function = {data_list}')

# sorting list berdasarkan banyaknya huruf dalam kata dengan len
data_list.sort(key=len)
print(f'sorted list by len = {data_list}')

# Sorting banyaknya huruf dalam kata menggunakan lambda
data_list = ['Otong', 'Ucup', 'Dudung']
data_list.sort(key=lambda nama: len(nama))  # key langsung diisi lambda
print(f'sorted list by lambda = {data_list}')

# * filter

data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# filter tanpa lambda
def kurang_dari_lima(angka):
    return angka < 5


data_angka_baru_fungsi = list(filter(kurang_dari_lima, data_angka))
print(f'filter dengan fungsi = {data_angka_baru_fungsi}')

# filter dengan lambda
data_angka_baru_lambda = list(filter(lambda x: x < 7, data_angka))
print(f'filter dengan lambda = {data_angka_baru_lambda}')
''' pemfilteran tanpa lambda perlu membuat fungsi terlebih dahulu, sedangkan dengan lambda dapat
    dipersingkat dengan tidak menggunakan fungsi'''

# memfilter angka genap dengan lambda
data_genap = list(filter(lambda angka: angka % 2 == 0, data_angka))
print(f'filter data genap = {data_genap}')

# memfilter angka ganjil dengan lambda
data_ganjil = list(filter(lambda angka: angka % 2 != 0, data_angka))
print(f'filter data ganjil = {data_ganjil}')

# memfilter angka kelipatan 3 dengan lambda
data_tiga = list(filter(lambda angka: angka % 3 == 0, data_angka))
print(f'filter kelipatan 3 = {data_tiga}')


# ** Anonymous function
''' teknik currying dibuat oleh haskell curry'''


# fungsi exponen biasa
def pangkat(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat(5, 2)
print(f'Hasil dengan fungsi biasa = {data_hasil}')


# dengan currying
def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)   # parameter dari fungsi pangkat diubah menjadi nilai 2
print(f'pangkat 2 dari 5 = {pangkat2(5)}')
''' penggunaan fungsi setelah nilai parameter didefinisikan'''

pangkat3 = pangkat(3)
print(f'pangkat 3 dari 4 = {pangkat3(4)}')

print(f'pangkat bebas = {pangkat(3)(5)}')
''' 3 adalah nilai parameter dan 5 adalah nilai yang dipangkatkan'''

'''
currying

def pangkat(n):
    return lambda angka: angka**n
    
pangkat3 = pangkat(3)   
print(f'pangkat 3 dari 4 = {pangkat3(4)}')

pangkat(3) = nilai 3 akan menjadi parameter/n pada fungsi pangkat
pangkat3(4) = nilai 4 dimasukkan ke variabel angka, dan karena n sudah didefinisikan 
              pada baris sebelumnya sehingga 4**3
              

'''
