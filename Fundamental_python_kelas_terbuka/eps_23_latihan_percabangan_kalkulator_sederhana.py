# latihan

print(20 * '=')
print('Kalkulator Sederhana')
print(20 * '=')

angka_1 = float(input('masukkan angka pertama: '))
operator = input('masukkan operator (+,-,x,/): ')
angka_2 = float(input('masukkan angka kedua: '))

# percabangannya

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == 'x' or '*':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah {hasil}')
else:
    print('masukkan operator yang benar!!')

print('Akhir dari program, terima gaji')
