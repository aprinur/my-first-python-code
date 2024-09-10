from cuypy_app import queries_db, main
from datetime import datetime
date_format = "%d/%m/%Y"


#  Fungsi memasukkan kegiatan ke database
def insert():
    nama_kegiatan = input('Nama kegiatan: ')
    tempat = input('Tempat kegiatan: ')

    while True:
        date = input('Tanggal kegiatan (dd-mm-yyyy): ')
        try:
            tanggal = datetime.strptime(date, '%d-%m-%Y').date()
            break
        except ValueError:
            print("Format tanggal tidak valid. Silahkan coba lagi")

    save = queries_db.tambah_kegiatan(nama_kegiatan, tempat, tanggal)
    print(save)


def check():
    queries_db.fetch_item()


def delete():
    while True:

        kegiatan = queries_db.fetch_item()
        if kegiatan == 0:
            main.main()
        else:
            nama_kegiatan = input('Masukkan nama kegiatan: ')
            queries_db.hapus(nama_kegiatan)

            verifikasi = input('Apakah akan lanjut menghapus [y/n] : ')
            if verifikasi.lower() == 'y':
                pass
            elif verifikasi.lower() == 'n':
                break
            else:
                print('Opsi tidak tersedia')


def show():
    while True:
        menu = int(input('\nMenu:'
                         '\n1. Tampilkan kegiatan'
                         '\n2. Tambah kegiatan'
                         '\n3. Hapus kegiatan'
                         '\n4. Kembali ke menu utama'
                         '\n\n Silahkan pilih 1/2/3/4: '))
        if menu == 1:
            check()
        elif menu == 2:
            insert()
        elif menu == 3:
            delete()
        elif menu == 4:
            main.main()
        else:
            print('Nilai yang dimasukkan tidak valid')


if __name__ == '__main__':
    show()
