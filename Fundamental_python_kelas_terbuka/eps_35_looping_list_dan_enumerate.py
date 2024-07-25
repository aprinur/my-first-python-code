
# * looping dengan for loop
kumpulan_angka = [3, 5, 7, 3, 5,]

print('For loop ')
for angka in kumpulan_angka:
    print(f'angka = {angka}')

peserta = ['ucup', 'otong', 'dadang', 'diding', 'dudung']

for nama in peserta:
    print(f'nama = {nama}')

# * looping dengan for dan range
kumpulan_angka = [3, 5, 7, 3, 5, 1,]

print('\nFor loop dan range')
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')


# * looping dengan while

print('\nWhile loop ')

kumpulan_angka = [3, 5, 7, 3, 5, 1,]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# * list comprehension

print("\nList comprehension")
data = ['otong', 3, 5, 7, 3, 5, 1, 'ujang']

[print(f'data = {i}') for i in data]   # pendefinisian list comprehension menggunakan kurung siku

angka = [3, 5, 7, 3, 5, 1,]

angka_kuadrat = [i ** 2 for i in angka]
print(angka_kuadrat)


# * Enumerate
# enumerate berfungsi untuk mendapatkan nomor index data
print('\nEnumerate')
data_list = ['otong', 3, 5, 7, 3, 5, 1, 'ujang']

for index, data in enumerate(data_list):
    print(f'index ke {index}, datanya adalah {data}')
