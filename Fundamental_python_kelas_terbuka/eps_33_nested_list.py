# nested list / list bersarang / list didalam list

data_0 = [1, 2]
data_1 = [3, 4, 5]

list_biasa = [1, 2, 3, 4]

print(f'list biasa = {list_biasa}')

list_2d = [data_0, data_1]  # list bisa dicampur dengan tipe data lainnya
print(f'list 2D = {list_2d}')

# contoh penggunaan

peserta_0 = ['Ucup', 25, 'Laki-laki']
peserta_1 = ['Otong', 10, 'Laki-laki']
peserta_2 = ['Meyrida', 20, 'Wanita']

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f'Peserta = {list_peserta}\n')

# salah satu cara menampilkan isi nested list

for peserta in list_peserta:
    print(f'Nama\t: {peserta[0]}')  #
    print(f'Umur\t: {peserta[1]}')
    print(f'Gender\t: {peserta[2]}\n')
''' peserta = nama_global variabel pengganti untuk setiap item didalam variabel list peserta
    peserta[0] untuk memanggil item pertama dari variable peserta
'''
# tidak semua operasi bisa dilakukan dengan nested list, salah satunya copy()
