import datetime


# sample data mulitkeys ( beraneka tipe data )
mahasiswa1 = {
    'nama_global': 'Ucup Surucup',
    'nim': '19100263',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 1, 13)
}

mahasiswa2 = {
    'nama_global': 'Otong Surotong',
    'nim': '19100264',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(1999, 9, 10)
}

mahasiswa3 = {
    'nama_global': 'Icuy Curucuy',
    'nim': '19100265',
    'sks_lulus': 100,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 2, 29)
}

data_mahasiswa = {

    'MAH001': mahasiswa1,  # Nested dictionary.
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}
''' 
    Nesting dictionary adalah dictionary didalam dictionary. 
    Value dari nested dictionary mengacu pada sebuah dictionary 
'''


# membuat tabel seperti pada database
print(f"{'KEY':<6} {'NAMA':<17} {'NIM':^10} {'SKS':<5} {'BEASISWA':<9} {'LAHIR':9}")
print('=' * 60)

# menampilkan setiap data pada data mahasiswa dengan for loop
for mahasiswa in data_mahasiswa:
    key = mahasiswa
    nama = data_mahasiswa[key]['nama_global']
    # mengambil key 'nama_global' dari nested dictionary yang ada dalam data_mahasiswa
    nim = data_mahasiswa[key]['nim']
    sks = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    # variabel diatas ditampilkan dalam bentuk tabel dibawah ini
    print(f"{key:<6} {nama:<17} {nim:^10} {sks:<5} {beasiswa:^9} {lahir:9}")
'''
    FORMAT STRING
    
    :< = Rata kiri
    :^ = Center
    :> = Rata kanan 
'''
