import datetime as dt  # memanggil library datetime sebagai dt

# cara menampilkan tanggal hari ini
hari_ini = dt.date.today()
# date adalah class dari library datetime, today adalah method dari class date
print(hari_ini)
print(f" hari ini adalah hari = {hari_ini:%A}")
# %A untuk menampilkan nama_global hari
# %a untuk menampilkan 3 huruf pertama dari nama_global hari

tanggal = dt.date(1945, 8, 17)
print(f" Tanggal {tanggal} adalah hari {tanggal:%A}")

# latihan
print('\n' + "LATIHAN".center(30, '='))

print('Silahkan masukkan tanggal, bulan dan tahun lahir ')
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
sisa_hari = ((umur_hari.days % 365) % 30)
print(f"Umur anda adalah: {umur_tahun} tahun,"
      f" {umur_bulan} bulan,"
      f" {sisa_hari} hari,"
      f" harinya adalah : {tanggal_lahir:%A}")
