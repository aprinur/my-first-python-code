"""Cara meminta input user"""


data = input('Masukkan data: ')
# Menggunakan fungsi input, lalu value yang dimasukkan akan disimpan ke variabel data
print('data =', data, 'type = ', type(data))
# data yang disimpan akan selalu bertipe string, jika membutuhkan data integer
# maka perlu casting data/ mengubah data
angka = int(input('Masukkan angka: '))
print('data =', angka, 'type = ', type(angka))

# Boolean
biner = bool(int(input('Masukkan nilai boolean: ')))
print('data =', biner, 'type = ', type(biner))
''' Biner/binary hanya terdiri dari 1 dan 0 yang merepresentasikan true dan false'''
