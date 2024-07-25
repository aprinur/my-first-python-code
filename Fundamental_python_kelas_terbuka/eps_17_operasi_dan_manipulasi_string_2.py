# operator dalam bentuk methods

# * merubah case dari string

# merubah semua ke upper case

salam = 'bro!'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

# merubah semua ke lower case

alay = "aKu KeCe AbieeeSssSSZZZZzz"
print("\nnormal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# * pengecekan dengan isX method

# contoh pengecekan lower case
salam = 'sist'
apakah_lower = salam.islower()  # hasilnya akan boolean
print('\n' + salam + 'is lower = ' + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilnya akan boolean
print(salam + ' is upper = ' + str(apakah_upper))


# isalpha() <-- untuk mengecek jika semuanya huruf
# isalnum() <-- untuk mengecek jika semua huruf dan angka
# isdecimal() <-- untuk mengecek jika semua angka
# isspace() <-- untuk mengecek jika kosong ( spasi, tab, newline \n )
# istittle <-- untuk mengecek jika semua kata diawali dengan huruf besar

judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle()  # hasil boolean
print(judul + 'is tittle = ' + str(cek_judul))


# * pengecekan dengan startswith() dan endswith()
cek_start = 'Sangjanim Oppa'.startswith('Sangjanim')  # bisa pengecekan degan kata
print('\nstart = ' + str(cek_start))
cek_start = 'Sanngjanim Oppa'.startswith('S')  # bisa pengecekan dengan huruf
print('start = ' + str(cek_start))

cek_end = 'Sanngjanim Oppak'.endswith('Oppak')  # bisa pengecekan degan kata
print('\nend = ' + str(cek_end))
cek_end = 'Sanngjanim Oppak'.endswith('k')  # bisa pengecekan dengan huruf
print('end = ' + str(cek_end))


# * penggabungan dan pemisahan komponen dengan join() dan split()
pisah = ['aku', 'dia', 'dan', 'mereka']
gabungan = ','.join(pisah)  # penggabungan dengan karakter koma
print('\n')
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)  # penggabungan dengan karakter spasi
print(gabungan)

gabungan = 'ehm'.join(pisah)
print(gabungan)

gabungan = 'akuehmdiaehmdanehmmereka'
print(gabungan.split('ehm'))
# hasil pemisahan akan menjadi list dan karakter 'ehm' akan hilang


# * alokasi karakter dengan rjust(), ljust(), dan center()

# rjust()
kanan = 'kanan'.rjust(10)  # cara lain penulisan method tanpa mendefinisikan suatu variabel
print("\n'" + kanan + "'")  # karakter akan menempel dikanan dengan jumlah karakter 10

# ljust()
kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")  # karakter akan menempel dikiri dengan jumlah karakter 10

# center()
tengah = 'tengah'.center(20, '=')
print("'" + tengah + "'")
""" karakter akan berada ditengah dengan sisi kanan dan kiri diisi '=',
    apabila tidak diisi maka akan otomatis terisi spasi"""

# mengembalikan dengan strip()

tengah = tengah.strip('=')  # menghilangkan tanda "=" atau karakter spasi apabila default
print("'" + tengah + "'")
