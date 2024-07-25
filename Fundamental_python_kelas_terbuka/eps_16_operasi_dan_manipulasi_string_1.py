# Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'Ucup'
nama_tengah = 'D'
nama_akhir = 'Fame'

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
# salah satu cara memberikan spasi atau karakter kosong dan tanda petik
print('\n' + nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)  # menggunakan fungsi len() untuk menghitung banyak karaker
print("\npanjang dari " + nama_lengkap + ' = ' + str(panjang) + " karakter \n")
# jumlah karakter termasuk spasi

# 3. Operator untuk string

# mengecek apakah ada atau tidak ada komponen char atau string pada suatu string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))
# menghasilkan False karena karakter d yang ada pada nilai dari variabel nama_lengkap adalah uppercase

D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))
# menghasilkan True karena karakter D uppercase ada pada nilai dari variable nama_lengkap

d = "d"
status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status), '\n')
# menghasilkan True karena karakter d lowercase tidak ada di variabel nama_lengkap


# mengulang string

print('wk' * 10)
print(15 * 'wk', '\n')  # posisi bisa dibalik

# indexing
# index dimulai dari 0
print("index ke 0 : " + nama_lengkap[0])  # merujuk ke index ke 0
print("index ke 6 : " + nama_lengkap[6])  # merujuk ke index ke 6
print("index ke (-1) : " + nama_lengkap[-1])  # merujuk ke karakter terakhir
print("index ke (-2) : " + nama_lengkap[-2])  # merujuk ke karakter kedua dari akhir
print("index ke [0:3] : " + nama_lengkap[0:4])  # mulai dari index ke 0 sampai index ke 4-1
print("index ke [3:7] : " + nama_lengkap[3:8])  # mulai dari index ke 3 sampai index ke 8-1
print("index ke [0,2,4,6,8,10] : " + nama_lengkap[0:11:2])
# mulai dari index ke 0 sampai index ke 11-1 dengan increment 2
# [start:stop:step]


# mencari item paling kecil berdasarkan nilai ascii code
print('\npaling kecil berdasarkan nilai ascii code : ' + min(nama_lengkap))
# mencari item paling besar berdasarkan nilai ascii code
print('paling besar berdasarkan nilai ascii code : ' + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char untuk ASCII dengan nomor 117 adalah : " + chr(data))


# 4. operator dalam bentuk method
data = "otong surotong pararotong"
print('\n' + data)
jumlah = data.count('o')
print("jumlah o pada " + data + ' = ' + str(jumlah))
