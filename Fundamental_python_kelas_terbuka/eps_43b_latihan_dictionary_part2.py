import datetime  # library untuk tanggal
import string   # library untuk karakter/string
import random   # library untuk mengacak
# * contoh penggunaan fromkeys

# template dict mahasiswa
mahasiswa_template = {  # iterable
    'nama_global': 'nama_global',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^20}")  # ^20 = membuat tulisan menjadi ditengah dengan 20 total karakter
print(f"{'DATA MAHASISWA':^20}")  # termasuk karakter spasi
print('=' * 20)
while True:
    # membuat dictionary berdasarkan key dari dictionary yang sudah ada
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())    # penggunaan fromkeys()
    ''' fromkeys() digunakan untuk membuat dictionary baru berdasarkan key dari 
        iterable yang diberikan.
        '''
    # meminta input value untuk dipasangkan ke key yang sudah ada
    mahasiswa['nama_global'] = input('Nama mahasiswa: ')
    mahasiswa['nim'] = input('NIM mahasiswa: ')
    mahasiswa['sks_lulus'] = int(input('SKS Lulus: '))
    tahun_lahir = int(input("Tahun lahir (yyyy): "))
    bulan_lahir = int(input("Bulan lahir (1-12): "))
    tanggal_lahir = int(input("Tanggal Lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    key = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    # membuat 6 random string ascii uppercase sebagai key

    data_mahasiswa.update({key: mahasiswa})  # mengupdate dictionary setiap ada data baru

    print(f"\n{'KEY':<6} {'NAMA':<17}{'NIM':<10} {'SKS':<5} {'LAHIR':9}")
    print('=' * 50)

    for mahasiswa in data_mahasiswa:
        key = mahasiswa
        nama = data_mahasiswa[key]['nama_global']
        nim = data_mahasiswa[key]['nim']
        sks = data_mahasiswa[key]['sks_lulus']
        lahir = data_mahasiswa[key]['lahir'].strftime("%x")
        # menampilkan value dari nested dictionary yang telah ditampung kedalam variabel
        print(f"{key:<6} {nama:<17} {nim:<10} {sks:<5} {lahir:9}")

    print('\n')
    is_done = input('Lanjut input? (y/n): ')
    if is_done == 'n':
        break

print('\n Akhir dari program')
