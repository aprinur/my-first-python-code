# Latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print('\nPROGRAM KONVERSI TEMPERATUR\n')

celcius = float(input('Masukkan suhu dalam celcius: '))
print('Suhu adalah', celcius, 'Celcius')

# Reamur = ( 4/5 ) * celcius
reamur = (4 / 5) * celcius
print('Suhu dalam reamur adalah', reamur, 'Reamur')

# Fahrenheit = ( 9/5 ) * celcius
fahrenheit = ((9 / 5) * celcius) + 32
print('Suhu dalam fahrenheit adalah', fahrenheit, 'Fahrenheit')
# ((9/5) * celcius) + 32 : ditambah kurung agar dieksekusi terlebih dahulu

# Kelvin = celcius + 273
kelvin = celcius + 273
print('Suhu dalam kelvin adalah', kelvin, 'Kelvin')


''' Latihan konversi fahrenheit ke kelvin viseversa '''
# Kelvin --> Fahrenheit
kelvin = float(input('Masukkan suhu kelvin: '))
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print('Suhu dalam fahrenheit adalah ', fahrenheit, 'Fahrenheit')

# Fahrenheit --> Kelvin
fahrenheit = float(input('Masukkan suhu fahrenheit: '))
celcius = 5/9 * (fahrenheit - 32)
kelvin = celcius + 273
print('Suhu dalam Kelvin adalah ', kelvin, 'Kelvin')
