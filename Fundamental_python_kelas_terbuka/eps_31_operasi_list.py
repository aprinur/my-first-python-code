
data_angka = [2, 5, 8, 4, 9, 1, 3, 6, 4, 2, 1, 5, 6, 4, 3, 7, 9]

print(f'data angka = {data_angka}')

# * mencari banyaknya value yang ada pada suatu data

jumlah_data_2 = data_angka.count(2)     # method .count() digunakan untuk mencari banyaknya nilai
# dalam suatu data
jumlah_data_4 = data_angka.count(4)     # method .count() digunakan untuk mencari banyaknya nilai
# dalam suatu data

print(f'banyaknya angka 2 dalam data_angka = {jumlah_data_2}')
print(f'banyaknya angka 4 dalam data_angka = {jumlah_data_4}')
print(f'banyaknya angka 3 dalam data_angka = {data_angka.count(3)}')


# * mencari posisi data (index)

data = ['Ucup', 'Otong', 'Dudung', 'Ujang']

print(f'data = {data}')

index_dudung = data.index('Dudung')  # method .index() digunakan untuk mencari nomor index data
print(f'index si dudung = {index_dudung}')
print(data.index('Otong'))

# * mengurutkan list ascending

print(f'data angka sebelum diurutkan = {data_angka}')
data_angka.sort()   # method .sort() berfungsi mengurutkan list secara ascending

print(f'data string sebelum diurutkan = {data}')
data.sort()     # method .sort() berfungsi mengurutkan list secara ascending
print(f'data string setelah diurutkan = {data}')
# data string akan diurutkan huruf depannya berdasarkan alfabet

# mengurutkan list descending

data_angka.reverse()  # method .reverse() berfungsi mengurutkan list secara descending
print(f'data angka setelah diurutkan terbalik/descending = {data_angka}')

print(f'data string dengan urutan ascending= {data}')
data.reverse()
print(f'data string dengan urutan ascending= {data}')

'''
    - method .count() digunakan untuk mencari banyaknya nilai dalam suatu data
    - method .index() digunakan untuk mencari nomor index data
    - method .sort() berfungsi mengurutkan list secara ascending
    - method .reverse() berfungsi mengurutkan list secara descending
'''