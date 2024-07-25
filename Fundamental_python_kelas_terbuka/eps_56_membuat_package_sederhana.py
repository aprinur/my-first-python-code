
# * cara cara pemanggilan package

import package_eps_56.matematika  # mengimport module matematika dari package 'package_eps_56'
""" cara mengimport ini memerlukan penulisan sumber fungsi saat akan digunakan contoh :
    package_eps_56.matematika.tambah 
    dimana 'package_eps_56' adalah nama package, 'matematika' adalah nama module, dan 'tambah'
    adalah nama fungsi
"""

from package_eps_56 import fisika  # mengimport module fisika dari package 'package_eps_56'
"""penggunaan fungsi dalam package ini lebih efisien karena hanya memerlukan nama modul dan 
   fungsi yang digunakan. contoh:
   fisika.gaya
   yang mana 'fisika' adalah module dan 'gaya' adalah fungsi  
"""

from package_eps_56.matematika import pangkat
# mengambil fungsi 'pangkat' dari module 'matematika' didalam package 'package_eps_56'

from package_eps_56.matematika import kali as mul  # bisa juga menggunakan as/alias
# mengambil fungsi 'kali' sebagai 'mul' dari module 'matematika' yang berada didalam
# package  'package_eps_56'


# * Penggunaan module dari package

hasil_tambah = package_eps_56.matematika.tambah(1, 2, 3, 4, 5)
print(f'hasil tambah dari package adalah = {hasil_tambah}')

gaia = fisika.gaya(90, 10)  # 'gaya' adalah fungsi didalam module 'fisika'
print(f'gaya adalah = {gaia}')

pangkat_3 = pangkat(3)
print(f'Pangkat 3 dari 8 adalah {pangkat_3(8)}')

print(f'Perkalian dari 8 * 7 adalah {mul(8, 7)}')

"""
didalam suatu package terdapat folder __pycache__ yang berfungsi untuk menyimpan bytecode 
yang telah dikompilasi. file bytecode ini berfungsi untuk mempercepat waktu eksekusi program dengan 
menghindari proses parsing dan kompilasi ulang kode sumber setiap kali program dijalankan

"""