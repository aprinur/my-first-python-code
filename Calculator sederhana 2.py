
def kalkulasi():

    while True:
        a = float(input('\nMasukkan nilai yang akan dikalkulasi :'))
        c = input('Masukkan lambang operator(+,-,*,/,%,//) : ')
        b = float(input('Masukkan nilai pengkalkulasi : '))

        if c == '+':
            d = a + b
            print(d)
            return d
        elif c == '-':
            d = a - b
            print(d)
            return d
        elif c == '*':
            d = a * b
            print(d)
            return d
        elif c == '/':
            d = a / b
            print(d)
            return d
        elif c == '%':
            d = a % b
            print(d)
            return d
        elif c == '//':
            d = a // b
            print(d)
            return d

        else:
            print('Lambang operator tidak valid')
            return


print('\n')

kalkulasi()

print('\n1. Lanjut kalkulasi ')
print('2. Stop')

x = input('Masukkan opsi yang dipilih (1/2) : ')
if x == '1':
    kalkulasi()
else:
    print('Kalkulasi dihentikan')
