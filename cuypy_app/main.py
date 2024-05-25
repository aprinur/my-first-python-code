from cuypy_app import cuypy_game, circle_calculator, simple_calculator, kegiatan_db
from cuypy_libs import welcome


def menu():
    while True:
        option = int(input('\n Perhatikan menu berikut '
                           '\n\n1. Cuypy game '
                           '\n2. Calculator sederhana '
                           '\n3. Menghitung luas keliling dan lingkaran'
                           '\n4. Membuat task to do '
                           '\n5. Hentikan program '
                           '\n\nMasukkan pilihan anda: '))

        if option == 1:
            cuypy_game.start()
        elif option == 2:
            simple_calculator.kalkulasi()
        elif option == 3:
            circle_calculator.calculate_circle()
        elif option == 4:
            kegiatan_db.show()
        elif option == 5:
            print('Program dihentikan')
            exit()
        else:
            print('Hanya bisa memilih nomor yang ada pada menu')


def main():
    welcome('SELAMAT DATANG DI CUYPY APP ')
    menu()


if __name__ == '__main__':
    main()
