# * Contoh penggunaan beberapa standard library


# Penggunaan library datetime

import datetime

data_waktu = datetime.datetime.now()
print(f'datetime now = {data_waktu}')
print(f'tahun = {data_waktu.year}')
print(f'bulan = {data_waktu.month}')
print(f'tanggal = {data_waktu.day}')
print(f'hari = {data_waktu.strftime('%A')}')


# Penggunaan library counter

from collections import Counter

data = ['a', 'b', 'c', 'd', 'a', 'l', 'b', 'c', 's']

# menghitung banyaknya karakter tertentu didalam list tanpa Counter
count = 0
for i in data:
    if i == 'b':
        count += 1

print(count)

# menghitung banyaknya karakter didalam list dengan Counter
jumlah = Counter(data)
print(f'Data count = {jumlah}')
print(f'Jumlah a = {jumlah['a']}')
print(f'Jumlah d = {jumlah['d']}')


# Membaca file external

import io

file = io.open('file_text_sample_eps_58.txt', 'r')
print(file.read())