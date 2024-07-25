# method ini sebagai front end

from . import Operasi


def delete_console():
    read_console()
    while True:
        print('Silahkan pilih nomor buku yang akan didelete')
        no_buku = int(input('Nomor buku: '))
        # memasukkan data dari nomor yang telah dipilih user ke variabel
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            # mengurai isi variabel dari nomor yang dipilih user
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # menampilkan data yang ingin dihapus
            print('\n' + '=' * 100)
            print(f'1. Judul\t: {judul:.40}')
            print(f'2. Penulis\t: {penulis:.40}')
            print(f'3. Tahun\t: {tahun:4}')

            # mengkonfirmasi pilihan user
            is_done = input('Apakah data yakin akan dihapus (y/n)?: ')
            if is_done.lower() == 'y':
                Operasi.delete(no_buku)
                break
        else:
            print('Nomor tidak valid, silahkan masukkan lagi')

    print('Data berhasil dihapus')


def update_console():
    read_console()  # menampilkan database terkini yang akan diupdate
    while True:
        print('Silahkan pilih nomor buku yang akan diupdate')
        no_buku = int(input('Nomor buku: '))

        # membaca data dari index yang telah dimasukkan
        data_buku = Operasi.read(index=no_buku)

        # memastikan jika data ada di database
        if data_buku:
            break
        else:
            print('Nomor tidak valid, silahkan masukkan lagi')

    # memisah lalu menguraikan data untuk diupdate
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]  # mengambil data dari index ke 4 sampai terakhir dari belakang

    while True:
        # menampilkan data untuk diupdate
        print('\n'+'='*100)
        print('Silahkan pilih data apa yang ingin anda ubah')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')

        # memasukkan data baru
        user_option = input('Pilih data [1,2,3]: ')
        print('\n' + '=' * 100)
        match user_option:
            case '1': judul = input('judul\t: ')
            case '2': penulis = input('penulis\t: ')
            case '3':
                while True:
                    try:
                        tahun = int(input('Tahun\t: '))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('Tahun harus 4 digit (yyyy) dan angka,silahkan masukkan tahun lagi')

                    except:
                        print('Tahun harus 4 digit (yyyy) dan angka, silahkan masukkan tahun lagi')
            case _: print('index tidak cocok')

        print('Data baru anda:')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. Penulis\t: {penulis:.40}')
        print(f'3. Tahun\t: {tahun:4}')

        is_done = input('Apakah data sudah sesuai (y/n)?: ')
        if is_done.lower() == 'y':
            break
    # menjalankan fungsi update dengan parameter yang telah disiapkan
    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print('\n\n' + '=' * 100)
    # meminta input dari user sebagai parameter
    print('Silahkan tambah data buku\n')
    penulis = input('Penulis\t: ')
    judul = input('Judul\t: ')
    while True:
        try:
            tahun = int(input('Tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun harus 4 digit (yyyy) dan angka,silahkan masukkan tahun lagi')

        except:
            print('Tahun harus 4 digit (yyyy) dan angka, silahkan masukkan tahun lagi')

    # menjalankan fungsi create dengan parameter yang telah dimasukkan
    Operasi.create(tahun, judul, penulis)
    print('\nBerikut adalah data baru anda')
    read_console()  # menampilkan database setelah data dimasukkan


def read_console():
    data_file = Operasi.read()  # menjalankan fungsi 'read()'

    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = "Tahun"

    # Header
    print('\n' + '=' * 100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    ''' judul:40 = membuat 40 karakter termasuk nilai dari judul, sisanya diisi spasi.
    cek eps_18_format_string baris 45 sampai 56'''
    print('-' * 100)

    # Data
    # memasukkan data kedalam variabel
    for index, data in enumerate(data_file):

        data_break = data.split(',')  # memisah data berdasarkan tanda koma

        # menguraikan data kedalam variabel
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]  # nilai index ke 2 dimasukkan kedalam variabel penulis
        judul = data_break[3]
        tahun = data_break[4]

        # menampilkan data yang sudah ditata agar sesuai dengan header
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}', end='')

    # Footer
    print('=' * 100 + '\n')