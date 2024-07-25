# # Tutorial membaca file eksternal

print('\n', ' Membaca file txt '.center(30, '='))

file = open('eps_64_sample_document.txt', mode='r')
"""Membuka file 'eps_64_sample_document.txt' dengan mode read (r)"""

print(f'status read = {file.readable()}')
""" method .readable() untuk mengecek apakah file bisa dibaca hasilnya adalah boolean.
bisa atau tidaknya tergantung mode yang digunakan saat membuka file (r/w)"""

print(f'status write = {file.writable()}')
""" method .writable() untuk mengecek apakah file bisa ditulis hasilnya adalah boolean,
bisa atau tidaknya tergantung mode yang digunakan saat membuka file (r/w)"""


# *membuka file
# print(file)


# * membaca seluruh file dengan method .read()
# print(file.read())


# * membaca file perbaris
# print(file.readline())  # membaca baris pertama
# print(file.readline())  # membaca baris kedua
'''file akan meng enter otomatis'''


# * membaca file perbaris tanpa enter
print(file.readline(), end='')  # membaca baris pertama
print(file.readline(), end='')  # membaca baris kedua
""" end='' menghilangkan enter setelah baris"""


# * membaca semua baris sebagai list
# print(file.readlines())  # semua hasil akan keluar sebagai list
# print(file.readlines()[1])  # menampilkan list ke 2

""" Setiap membuka file harus selalu ditutup"""

# * mengecek apakah file sudah ditutup menggunakan .closed
print(f'apakah file sudah diclose : {file.closed}')  # hasil boolean

# * menutup file setelah dibuka
file.close()
print(f'apakah file sudah diclose : {file.closed}')  # hasil boolean


# * membuka file agar tidak perlu melakukan penutupan file

print('\n', " Membaca file txt dengan 'with'".center(42, '='))

with open("eps_64_sample_document.txt", mode='r') as file:
    content = file.readline()
    print(content, end='')
    print(f'apakah file sudah diclose : {file.closed}')

"""file hanya terbuka didalam with statement dan akan tertutup otomatis saat keluar dari statement
   with"""
