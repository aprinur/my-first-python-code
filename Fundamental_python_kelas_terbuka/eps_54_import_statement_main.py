# import

""" Import berfungsi untuk mengambil program dari file external berekstensi .py"""

# Penggunaan import

# 1. Untuk menyambung program dari eksternal

import eps_54_program_print
import eps_54_program_ucup


# 2. Import dengan data
import eps_54_variable
import eps_54_trial

# data ada di namespace variable
print(eps_54_variable.data)
print(eps_54_trial.data)
''' name space berfungsi agar apabila ada nama data yang sama, maka data pertama tidak 
    akan tertimpa data setelahnya 
'''

# 3. Import dengan fungsi
import eps_54_math

hasil = eps_54_math.tambah(9, 8)  # eps_54_math -> pada variabel disamping disebut namespace
print(hasil)