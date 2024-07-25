# program list buku

list_buku = []

while True:
    print('\nMasukkan data buku')
    judul = input('Judul buku \t\t:')   # meminta input data buku
    penulis = input('Nama penulis\t:')  # meminta input data buku

    buku_baru = [judul, penulis]    # memasukkan nilai variabel judul & penulis ke list buku_baru
    list_buku.append(buku_baru)  # Menambahkan buku_baru ke list_buku

    print("\n\n", '=' * 10, 'Data Buku', '=' * 10)
    for index, buku in enumerate(list_buku):    # Menampilkan isi list_buku
        print(f'\n {index+1} | {buku[0]} | {buku[1]}')  # Menampilkan isi list_buku

    print("\n\n", '=' * 31)
    islanjut = input('Apakah akan dilanjutkan? (y/n): ')

    if islanjut == 'n':  # konfirmasi kelanjutan input
        break

print('Program selesai')