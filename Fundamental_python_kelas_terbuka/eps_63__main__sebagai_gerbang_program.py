# __main__ adalah top level code enviroment

"""
__main__ pada suatu program menandakan apabila program itu adalah program utama (main = utama)
"""

# __name__ = "__main__" akan terjadi jika ada di file program utama

# __name__ pada file program utama
print(f"nilai __name__ pada eps_63__main__sebagai_gerbang_program.py = '{__name__}'")
''' __name__ pada baris diatas akan berubah menjadi __main__ karena program ini akan dianggap 
sebagai program utama '''

# __name__ pada file program eksternal
import eps_63__main__sebagai_gerbang_program_fungsi
'''saat dijalankan __name__ akan berubah menjadi nama program eksternal tersebut, karena program 
eksternal tersebut dipanggil ke progaram utama'''


# * contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a: int, b: int) -> int:  # int = hint
    return a + b


# fungsi utama
if __name__ == "__main__":
    angka1 = 6
    angka2 = 8
    hasil = fungsi_tambah(angka1, angka2)
    print(f'hasil tambah = {hasil}')

'''
baris kode "if fungsi __name__ == '__main__'" berfungsi untuk menjalankan 
fungsi - fungsi yang telah dideklarasikan sebelumnya
 '''
