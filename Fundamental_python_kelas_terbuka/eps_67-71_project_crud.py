import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name  # mendeteksi sistem operasi

    # match sistem_operasi:
    #     case "posix": os.system('clear')
    #     case "nt": os.system('cls')

    print('\n' + ' SELAMAT DATANG DI PROGRAM '.center(40, '='))
    print(' DATABASE PERPUSTAKAAN '.center(40, '='))

    # check database ada atau tidak
    CRUD.init_console()

    while True:

        pilihan_user = (input('''
1. Read Data
2. Create Data
3. Update Data
4. Delete Data
                                 
Masukkan opsi (1/2/3/4): '''))  # meminta pilihan user

        match pilihan_user:
            case '1': CRUD.read_console()  # jika user memilih 1 maka read_console() dijalankan
            case '2': CRUD.create_console()  # jika user memilih 2 maka create_console() dijalankan
            case '3': CRUD.update_console()  # jika user memilih 3 maka update_console() dijalankan
            case '4': CRUD.delete_console()  # jika user memilih 4 maka delete_console() dijalankan

        print('=' * 40)

        # konfirmasi kelanjutan program
        is_done = input('Apakah Selesai (y/n)?: ')  # konfirmasi kelanjutan program
        if is_done.lower() == 'y':
            break

    print("Program Berakhir  ")