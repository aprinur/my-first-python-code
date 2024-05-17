
daftar_kegiatan = []


# Fungsi menampilkan
def menampilkan():
    print('\nDaftar kegiatan yang telah dibuat :')
    if not daftar_kegiatan:
        print('\nDaftar kegiatan kosong')
    else:
        for kegiatan in enumerate(daftar_kegiatan, start=1):
            print(kegiatan)


# Fungsi penambahan
def penambahan():
    kegiatan_baru = input('Masukkan nama kegiatan :')
    daftar_kegiatan.append(kegiatan_baru)

    print(f"\n{kegiatan_baru} telah ditambahkan ke daftar kegiatan")

# Fungsi Penghapusan

def penghapusan():
    if not daftar_kegiatan:
        print('\nDaftar kegiatan kosong')
        return

    menampilkan()
    hapus_kegiatan = input('\nMasukkan nama kegiatan yang akan dihapus :')

    if hapus_kegiatan in daftar_kegiatan:
        daftar_kegiatan.remove(hapus_kegiatan)
        print('\nKegiatan telah dihapus dari daftar')
    else:
        print('Nama kegiatan tidak ada dalam daftar kegiatan')


def task():

    while True:
        print('\nMenu:')
        print('1. Tampilkan daftar kegiatan')
        print('2. Tambahkan kegiatan')
        print('3. Hapus kegiatan')
        print('4. Keluar')

        pilihan = input('\nPilih menu nomor (1/2/3/4) : ')

        if pilihan == '1':
            menampilkan()
        elif pilihan == '2':
            penambahan()
        elif pilihan == '3':
            penghapusan()
        elif pilihan == '4':
            print('\nAdios')
            break
        else:
            print('\nPilihan tidak valid')

        if __name__ == '__main__':
            task()


