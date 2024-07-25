"""
    Runtime error adalah error yang terjadi karena kondisi yang tidak diantisipasi atau kesalahan
        logika dalam kode. Error terjadi setelah program dieksekusi
    Syntax error terjadi karena kesalahan penulisan kode atau kesalahan logika penulisan kode.
        Error terjadi saat program dieksekusi, biasanya sudah ada warning saat proses penulisan
        kode
"""

# # contoh runtime error
# data_input = int(input('Masukkan angka: '))
# hasil = 10 / data_input
# print(hasil)
# saat dimasukkan angka 0 akan terjadi error, error tersebut disebut runtime error

# file = open('sample_data_eps_66.txt', 'r')
# secara penulisan syntax benar namun akan error karena file 'sample_data_eps_66.txt' tidak ada

# # contoh syntax error
# data_input = int(input('Masukkan angka: '))
# hasil = 10 / data_input
# print(hasil  # error karena kurang tanda kurung tutup pada syntax


""" exception akan terjadi pada saat mengalami runtime error"""

# contoh menangkap exception dengan try & except

user_input = int(input('Masukkan angka: '))
hasil = None

try:
    hasil = 10 / user_input
except:
    print(f'input tidak bisa 0')
''' try akan dieksekusi pertama kali lalu saat try mengalami error maka except akan dieksekusi.
    pada program diatas penyebab runtime error adalah karena membagai dengan 0 '''

print(f'hasil = {hasil}')


# 1. contoh dalam aplikasi

while True:
    angka = int(input('Masukkan angka pembagi: '))
    try:  # saat mengalami error di try maka akan menjalankan excepts
        hasil = 10 / angka
        print(f'hasil = {hasil}')
        is_done = input('lanjutkan ? (y/n): ')
        if is_done == 'n':
            break
    except:
        print('pembagi nol, silahkan masukkan input lagi!!')
""" setelah menampilkan pesan error pada except program akan melanjutkan perulangan dari awal"""

print('akhir dari program 1')


# 2. contoh dalam aplikasi

try:
    with open('sample_data_eps_66.txt', 'r') as file:
        print(file.read())
        # saat menjalankan program pertama kali akan error lalu lanjut membaca 'except'.
        # saat menjalankan program kedua kali maka akan membaca isi 'sample_data_eps_66.txt'
        # karena file sudah dibuat saat membaca 'except'.
except:
    print('file sample_data_eps_66.txt tidak ditemukan, membuat file baru')
    with open('sample_data_eps_66.txt', 'w', encoding='utf-8') as file:
        file.write('file baru')
""" saat mengeksekusi pertama kali akan membaca apabila file 'sample_data_eps_66.txt' tidak 
ada, lalu akan dibuat saat berada didalam except. Karena file sudah ada maka saat dieksekusi 
kedua kali tidak akan terjadi error jadi program didalam try akan dijalankan
"""
print('akhir dari program 2')