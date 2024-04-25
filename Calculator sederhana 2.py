def kalkulasi():

    while True:
        a = float(input('\nMasukkan nilai yang akan dikalkulasi :'))
        c = input('Masukkan lambang operator(+,-,*,/,%,//) : ')
        if c not in ['+', '-', '*', '/', '%', '//']:
            print('Lambang operator yang dimasukkan salah')
            continue
        else:
            b = float(input('Masukkan nilai pengkalkulasi : '))

            if c == '+':
                d = a + b
            elif c == '-':
                d = a - b
            elif c == '*':
                d = a * b
            elif c == '/':
                d = a / b
            elif c == '%':
                d = a % b
            elif c == '//':
                d = a // b

            print(f'Hasil kalkulasi = {d}')

            lanjutkan = input('\n1. Lanjut kalkulasi\n2. Hentikan Kalkulasi \nMasukkan opsi yang dipilih (1/2): ')
            if lanjutkan == '2':
                print('Kalkulasi dihentikan')
                break


kalkulasi()
