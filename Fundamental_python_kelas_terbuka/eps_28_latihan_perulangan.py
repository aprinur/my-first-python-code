# latihan perulangan membuat segitiga


# 1. Menggunakan for

sisi = 10
print('Awal for')
count = 1   # dummy variable
for i in range(sisi):
    print('+' * count)
    count += 1
'''
mengalikan karakter '+' dengan nilai dari variabel count, 
lalu nilai dari variabel count ditambah 1 dan melanjutkan perulangan sampai nilai dari 
variabel count sama dengan nilai dari variabel sisi
'''

print('akhir dari for')

# 2. Menggunakan while

print('\nAwal while')
count = 1  # dummy variable
while True:
    print('x' * count)
    count += 1

    if count > sisi:
        break

print('Akhir dari while')

# 3. segitiga hanya ganjil saja

print('\nawal while ganjil ')
sisi = 10
count = 1  # dummy variable

while True:
    if count % 2 != 0:  # pengecekan bilangan ganjil
        print('*' * count)
        count += 1
    else:   # jika bilangan genap
        count += 1

    if count == sisi:
        break

print('akhir dari while')

# 4. segitiga sama sisi hanya ganjil saja

print('\nawal while ganjil ')
sisi = 9
count = 1  # dummy variable
spasi = int(sisi/2)  # pembagian akan secara otomatis menjadi float jadi perlu casting ke integer

while True:
    if count % 2 != 0:  # pengecekan bilangan ganjil
        print(' ' * spasi, '+' * count)
        spasi -= 1
        count += 1
    else:   # jika bilangan genap
        count += 1

    if count == sisi:
        break

print('akhir dari while')


# 5. tugas membuat belah ketupat

sisi = 100
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2 != 0:
        print(' ' * spasi, 'X' * count)
        count += 1
        spasi -= 1
    else:
        count += 1

    if count == sisi:
        break

sisi = 0
count = 100
spasi = int((sisi+1) * 2)
while True:
    if count % 2:
        print(' ' * spasi, 'X' * count)
        count -= 1
        spasi += 1
    else:
        count -= 1

    if count == sisi:
        break
