import numpy as np

'''
Numpy adalah salah satu package python untuk operasi matematika khususnya matrix.
Matrix adalah susunan suatu bilangan satu atau lebih baris dan kolom yang membentuk segi empat 
vector adalah daftar angka yang membentuk baris atau kolom 
Menghitung ukuran matrix dimulai dari baris lalu kolom / Y * X / Tinggi x Lebar
Ukuran matrix disebut juga dengan ordo
Tiap bilangan didalam matrix disebut elemen matrix
'''

# * Penggunaan numpy untuk vector


list_a = [1, 2, 3, 4, 5, ]  # akan menjadi list biasa
vector_a = np.array([1, 2, 3, 4, 5])  # akan menjadi vector
print(list_a)
print(f'list_a = {list_a}')
print(vector_a)
print(f'vector_a = {vector_a}')
"""perbedaan utama antara vector dan list adalah setiap angka dalam list dipisahkan dengan koma 
   sedangakan vector dipisahkan dengan spasi biasa"""

# perbedaan list dan vektor apabila dikuadratkan dan dikalikan

# Dikuadratkan
"""print(list_a ** 2)"""  # akan terjadi eror karena yang dipangkatkan harus angka bukan variabel
print(vector_a ** 2)  # setiap elemen didalam vector akan dipangkatkan

# Dikalikan
print(list_a * 2)  # akan menampilkan nilai dari variabel sebanyak 2 kali
print(vector_a * 2)  # setiap elemen akan dikalikan 2


# * Penggunaan numpy untuk matrix


# membuat matrix 2 kolom dan 2 baris
matrix_b = np.array([(1, 2), (3, 4)])
print(f'matrix b = \n{matrix_b}')
print(f'matrix b^2 = \n{matrix_b ** 2}')  # memangkatkan 2 setiap angka didalam matrix

# Membuat matrix 0
zeros_c = np.zeros((2, 2))  # membuat matrix berisi nilai 0 dengan dengan ukuran 2 * 2
print(f'zeros c = \n{zeros_c}')

# Membuat matrix 1
ones_d = np.ones((2, 2))  # membuat matrix berisi elemen 1 dengan ukuran 2 * 2
print(f'ones d = \n{ones_d}')

# Penjumlahan matrix
jumlah = matrix_b + matrix_b ** 2 + ones_d
print(f'hasil = \n{jumlah}')   # setiap elemen akan dijumlahkan berdasarkan susunan matrix
