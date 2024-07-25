
""" __init__.py adalah file yang akan dieksekusi pertama kali saat mengimport package"""

import package_eps_57

""" saat mengimport package 'package_eps_57' yang diimport hanyalah foldernya namun 
modul/sub package yang ada di dalamya tidak termasuk, oleh karena itu modul yang akan digunakan 
harus ditambahkan di dalam file '__init__.py'. Cara lain untuk menjalankan progaram
tanpa mengimport keseluruhan module adalah seperti berikut :
"""

hasil_tambah = package_eps_57.matematika.basic.tambah(1, 2, 3, 4, 45)
print(f'hasil tambah = {hasil_tambah}')
""" mengakses fungsi 'tambah' dalam module 'basic' dari sub package 'matematika' yang berada 
dalam package 'package_eps_57
"""

pangkat_3 = package_eps_57.matematika.scientific.pangkat(3)
hasil_scientific = pangkat_3(5)
print(f'hasil dari pangkat 3 = {hasil_scientific}')
""" didalam package bernama 'package_eps_57' terdapat sub package bernama 'matematika', didalam
sub package 'matematika' terdapat module bernama 'scientific', didalam module 'scientific' 
terdapat fungsi 'pangkat'
"""

hasil_kali = package_eps_57.gaya(6, 6)
print(f'Hasil kali = {hasil_kali}')


"""
didalam package 'package_eps_57' terdapat package lagi bernama 'matematika', maka dari itu 
dalam file __init__.py dari package 'package_eps_57' perlu ditambahkan program untuk mengimport
package 'matematika' dan pada file __init__.py dalam package 'matematika' juga perlu ditambahkan 
program untuk mengimport module module yang ada didalamnya 

sehingga saat memanggil 'package_eps_57' alurnya menjadi:

import package_eps_57 --> __init__.py package_eps_57 --> package matematika -->

__init__.py package matematika --> module

#
"""

# from package_eps_57 import *  # tidak disarankan untuk dipakai
#
# """
# import * berpasangan dengan keyword __all__ pada file __init__.py berfungsi
# untuk mengimport module yang telah ditentukan didalam keyword __all__ """
#
# hasil_tambah = matematika.basic.tambah(1, 2, 3, 4, 45)
# print(f'hasil tambah = {hasil_tambah}')
#
# pangkat_3 = matematika.scientific.pangkat(3)
# hasil_scientific = pangkat_3(5)
# print(f'hasil dari pangkat 3 = {hasil_scientific}')
#
# # kode setelah fungsi 'gaya' dari module 'phisika' diimport pada file __init__.py
# hasil_kali = phisika.gaya(6, 6)
# print(f'Hasil kali = {hasil_kali}')
