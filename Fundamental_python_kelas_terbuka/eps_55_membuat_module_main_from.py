
# from eps_55_matematika import tambah, kali, pangkat  <-- mengimport fungsi pada modul
from eps_55_module_matematika import *
# tanda bintang digunakan untuk mengimport keseluruhan fungsi pada module

""" Jika menggunakan 'from' lalu dilanjutkan nama module yang dipanggil maka tidak perlu lagi
    menggunakan nama module saat menggunakan fungsi  """

hasil_tambah = tambah(1, 3, 4, 6, 7, 8)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = kali(2, 5, 1, 6, 4)
print(f'hasil kali = {hasil_kali}')

pangkat_3 = pangkat(3)
print(f'hasil pangkat 3 = {pangkat_3(3)}')