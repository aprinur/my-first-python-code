
# index= 0(-3)   1(-2)    2(-1)
data = ['Ucup', 'Otong', 'Dudung']

# mengambil data dari list
data_0 = data[0]    # mengambil data pertama dari list berdasarkan index ( index dimulai dari 0)
print(f'data pertama (index 0) = {data_0}')

data_terakhir = data[-1]
# contoh jika mengambil data terakhir namun data tidak diketahui jumlah datanya
print(f'data terakhir adalah = {data_terakhir}')

data_ucup = data[-3]
print(f'data ucup = {data_ucup}')

# mengambil info jumlah data dalam list
panjang_data = len(data)    # mencari jumlah data/panjang data dari list dengan len
print(f'panjang data = {panjang_data}')


# menambah item pada list sesuai posisi index
print(f'data sebelum ditambah = {data}')
data.insert(1, 'Asep')   # menambah item pada index ke 1
print(f'data sesudah ditambah = {data}')

# menambah item diakhir list
data.append('Jajang')   # menambah item pada posisi terakhir
print(f'data sesudah ditambah diakhir = {data}')

# menggabungkan list
data_baru = ['Ujang', 'Usep', 'Dadang']
data.extend(data_baru)
print(f'data gabungan = {data}')

# merubah data
# merubah data index ke 2 menjadi michael
data[2] = 'Michael'
print(f'data rubah = {data}')

# menghapus data
data.remove('Ujang')    # menghapus data Ujang. Besar kecil huruf harus sama dengan yang ada di data.
print(f'data remove = {data}')

# menghilangkan data terakhir
data_akhir = data.pop()
print(f'data akhir = {data}')
# pop secara default menghilangkan data terakhir namun bisa dipindahkan ke variabel lain
print(data_akhir)

