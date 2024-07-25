
# data
data_nama = 'Ucup Surucup'
data_umur = 17
data_tinggi = 159.3
data_nomor_sepatu = 43


# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor = {data_nomor_sepatu}"
print('Data String'.center(31, '='))
print(data_string)

# string multiline (dengan menggunakan enter atau newline (\n))
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor = {data_nomor_sepatu} "
print('\n' + 'Data String'.center(31, '='))
print(data_string)

# string multiline dengan triple double quotes atau single quotes
# akan menampilkan sesuai dengan posisi nilai di variabel
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor = {data_nomor_sepatu}
"""
print('\n' + 'Data String'.center(31, '='))
print(data_string)

# mengatur lebar
data_nama = 'ucup'
data_string = f"""
nama    = {data_nama}
umur    = {data_umur}
tinggi  = {data_tinggi}
nomor   = {data_nomor_sepatu}
"""
print('\n' + 'Data String'.center(31, '='))
print(data_string)

# mengatur rata kanan
data_nama = 'ucup'
data_string = f"""
nama    = {data_nama:>10}  
umur    = {data_umur}
tinggi  = {data_tinggi}
nomor   = {data_nomor_sepatu}
"""
# saat dicetak akan menampilkan 10 karakter dengan nilai variabel berada disisi kanan,
# sedangkan disisi kiri diisi spasi.
# simbol > bisa juga diganti dengan <.
print('\n' + 'Data String'.center(31, '='))
print(data_string)

data_nama = 'ucup'
data_tinggi = 120.48
data_string = f"""
nama    = {data_nama:>5}  
umur    = {data_umur:>5}
tinggi  = {data_tinggi:>5}
nomor   = {data_nomor_sepatu:>5}
"""
# jika jumlah karakter pada nilai dari suatu variabel melebihi jumlah karakter yang
# ingin ditampilkan, maka tetap akan ditampilkan apa adanya.
print('\n' + 'Data String'.center(31, '='))
print(data_string)