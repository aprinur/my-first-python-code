
"""
format penggunaan perulangan for:
for kondisi:
    aksi
"""

# perulangan for dengan list
angka2_list = [0, 2, 4, 6, 8, 10]  # contoh list
print(angka2_list)

for i in angka2_list:
    print(f' i sekarang = {i}')

print('akhri dari progaram 1\n')

# perulangan dengan range
angka2_range = range(5)  # contoh range.

for i in angka2_range:
    print(f'i sekarang = {i}')
# hasil yang ditampilkan hanya dari 0 sampai 4 tidak termasuk angka batas yang diberikan(5)
print('akhir dari program 2\n')

angka2_range = range(1, 10)

for i in angka2_range:
    print(f'i sekarang = {i}')

print('akhir dari program 3')

# perulangan dengan string
# secara otomatis akan menampilkan setiap karakter dari string yang disediakan

data_str = ('\noleh karena itu, penjajahan diatas dunia harus dihapuskan karena tidak sesuai dengan '
            'perikemanusiaan dan perikeadilan')
for huruf in data_str:
    print(huruf)
print('akhir dari program 4\n')
