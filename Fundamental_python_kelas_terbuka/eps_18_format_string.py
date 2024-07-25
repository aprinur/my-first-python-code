# * contoh generic

# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
print('\n')
boolean = False
format_str = f"contoh boolean = {boolean}"
print(format_str)

# angka
print('\n')
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# bilangan bulat
print('\n')
angka = 15
format_str = f'bilangan bulat = {angka:d}'
# d berfungsi untuk menunjukan jika variabel angka bernilai bilangan bulat/integer.
# tidak akan bermasalah meski tidak dipakai.
print(format_str)

# bilangan dengan ordo ribuan
print('\n')
angka = 20000000
format_str = f"ribuan = {angka:,}"  # untuk menampilkan koma pada ordo ribuan
# tanda koma akan secara otomatis muncul setiap 3 angka
print(format_str)

#  bilangan desimal
print('\n')
angka = 2005.57896
format_str = f'desimal = {angka:.2f}'
# .2f = untuk memunculkan hanya 2 angka dibelakang koma. angka 2 bisa diganti sesuai kebutuhan
print(format_str)

# menampilkan leading zero
print('\n')
angka = 2005.57896
format_str = f'desimal = {angka:8.3f}'
# 8.3f = menampilkan 8 karakter, 3 angka desimal (dibelakang koma) + titik + sisa angka didepan koma
# secara default jika jumlah angka dan karakter kurang dari jumlah yang ingin ditampilkan
# maka akan ditambahkan karakter putih (spasi)
print(format_str)
print('\n')
angka = 2005.57896
format_str = f'desimal = {angka:010.3f}'
# 010.3f = menampilkan 3 angka dibelakang koma(.3f), dengan total 10 karakter(10),
#          karakter spasi (apabila tidak diisi) akan diganti dengan angka 0 (0 didepan angka 10).
# jika nilai 0 didepan jumlah karakter yang ingin ditampilkan diganti angka lain,
# maka secara otomatis akan membuat spasi sebanyak nilai tersebut
print(format_str)

# menampilkan tanda + dan -
print('\n')
angka_minus = -10
angka_plus = 10
format_minus = f'minus = {angka_minus}'  # lambang minus akan secara otomatis ditampilkan
format_plus = f'plus = {angka_plus:+d}'  # untuk menampilkan lambang plus tambahkan +d

print(format_minus)
print(format_plus)
print('\n')
angka_plus = +10.514321
format_plus = f'plus = {angka_plus:+09.3f}'  # bisa digabung dengan bilangan desimal
print(format_plus)

# memformat persen
print('\n')
presentase = 0.045
format_persen = f"persen = {presentase:.2%}"
# lambang % mengubah menjadi presentase dan .2 agar hanya 2 angka dibelakang koma
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain ( binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)