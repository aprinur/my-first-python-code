from cuypy_app import cuypy_game, circle_calculator, simple_calculator
from cuypy_libs import welcome
from kegiatan import task
#  Fungsi menampilkan selamat datang

welcome('SELAMAT DATANG DI CUYPY APP ')


while True:
    try:
        menu = int(input('\n Perhatikan menu berikut '
                         '\n\n1. Cuypy game '
                         '\n2. Calculator sederhana '
                         '\n3. Menghitung luas keliling dan lingkaran'
                         '\n4. Membuat task to do '
                         '\n5. Hentikan program '
                         '\n\nMasukkan pilihan anda: '))

        if menu == 1:
            cuypy_game.start()
        elif menu == 2:
            simple_calculator.kalkulasi()
        elif menu == 3:
            circle_calculator.calculate_circle()
        elif menu == 4:
            task()
        elif menu == 5:
            print('Program dihentikan')
            exit()
        else:
            print('Hanya bisa memilih nomor yang ada pada menu')

    except ValueError:
        print('Masukkan pilihan yang valid(angka): ')
