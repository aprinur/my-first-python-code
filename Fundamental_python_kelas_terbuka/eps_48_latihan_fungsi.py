# * program menghitung luas dan keliling persegi panjang tanpa fungsi

"""
# Membuat header program
print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
print(f'{'='*40:^40}')

# Mengambil input user
lebar = int(input('Masukkan nilai lebar:'))
panjang = int(input('Masukkan nilai panjang: '))

# Program menghitung luas
luas = panjang * lebar
keliling = 2*(panjang+lebar)

# Menampilkan hasil
print(f'Hasil perhitungan luas = {luas}')
print(f'Hasil perhitungan keliling = {keliling}')
"""


# * Program menghitung luas dan keliling persegi panjang dengan fungsi

def header():
    """Fungsi header"""
    print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print(f'{'=' * 40:^40}')


def input_user():
    """Fungsi input user"""
    lebar = int(input('\nMasukkan nilai lebar:'))
    panjang = int(input('Masukkan nilai panjang: '))

    return lebar, panjang


def hitung_luas(lebar, panjang):
    """Fungsi perhitungan luas"""
    return lebar * panjang


def hitung_keliling(lebar, panjang):
    """Fungsi perhitungan keliling"""
    return 2 * (lebar + panjang)


def display(messege, value):
    """Fungsi display"""
    print(f'Hasil perhitungan {messege} = {value}')


# PR menambahkan opsi yang akan dihitung
def opsi_perhitungan():
    """Fungsi memilih perhitungan"""
    pilihan = input('''
1. Hitung luas
2. Hitung keliling
3. Hitung luas dan keliling
    
Masukkan pilihan (1/2/3): ''')
    return pilihan


while True:
    header()

    # PR menambahkan opsi yang akan dihitung
    opsi = opsi_perhitungan()
    if opsi == '1':
        Lebar, Panjang = input_user()
        luas = hitung_luas(Lebar, Panjang)
        display('Luas', luas)
    elif opsi == '2':
        Lebar, Panjang = input_user()
        keliling = hitung_keliling(Lebar, Panjang)
        display('Keliling', keliling)
    elif opsi == '3':
        Lebar, Panjang = input_user()
        luas = hitung_luas(Lebar, Panjang)
        keliling = hitung_keliling(Lebar, Panjang)
        display('Luas', luas)
        display('Keliling', keliling)
    else:
        print('Masukkan pilihan yang ada')

    iscontinue = input('\nApakan lanjut? (y/n): ')
    if iscontinue.lower() == 'n':
        break

print('\nPROGRAM SELESAI')

''' 
    Setiap fungsi memiliki tujuan tertentu sehingga tidak disarankan menggabung beberapa tujuan
    didalam satu fungsi.
    Penggunaan fungsi mempermudah maintenance program karena progaram sudah dibuat berdasarkan 
    tujuan tertentu.
'''
