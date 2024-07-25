import datetime

# * contoh penggunaan fromkeys

# template dict mahasiswa
mahasiswa_template = {  # iterable
    'nama_global': 'nama_global',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}

# membuat input user untuk mengisi dictionary

print(f"{'SELAMAT DATANG':^20}")  # ^20 = membuat tulisan menjadi ditengah dengan 20 total karakter
print(f"{'DATA MAHASISWA':^20}")  # termasuk karakter putih(spasi)
print('=' * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())    # penggunaan fromkeys()
''' fromkeys() digunakan untuk membuat dictionary baru berdasarkan key dari 
    iterable yang diberikan.
'''
# meminta input value untuk dipasangkan ke key yang telah ditentukan
mahasiswa['nama_global'] = input('Nama mahasiswa: ')
mahasiswa['nim'] = input('NIM mahasiswa: ')
mahasiswa['sks_lulus'] = int(input('SKS Lulus: '))
tahun_lahir = int(input("Tahun lahir (yyyy): "))
bulan_lahir = int(input("Bulan lahir (1-12): "))
tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
print(mahasiswa)
