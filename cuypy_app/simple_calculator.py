def kalkulasi():
    while True:
        a = float(input('\nMasukkan nilai yang akan dikalkulasi :'))
        c = input('Masukkan lambang operator(+,-,*,/,%,//) : ')
        if c not in ['+', '-', '*', '/', '%', '//']:
            print('Lambang operator yang dimasukkan salah')
            continue
        else:
            b = float(input('Masukkan nilai pengkalkulasi : '))
            d = []
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

        lanjutkan = int(input('\n1. Lanjut kalkulasi'
                              '\n2. Hentikan Kalkulasi '
                              '\n\nMasukkan opsi yang dipilih (1/2): '))
        while lanjutkan not in [1, 2]:
            lanjutkan = int(input('Masukkan sesuai opsi yang tersedia: '))

        if lanjutkan == 2:
            print('Kalkulasi dihentikan')
            break

        return lanjutkan


if __name__ == '__main__':
    kalkulasi()
