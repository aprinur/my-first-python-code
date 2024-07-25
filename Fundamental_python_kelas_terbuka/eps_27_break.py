"""
break = break berfungsi untuk menghentikan program
"""

# contoh penggunaan 1

angka = 0

while True:
    angka += 1
    print(f'angka sekarang = {angka}')

    if angka == 3:
        print("nice!")
        break

    print('Hola')

print('Kelar / done')
'''
break akan menghentikan program perulangan saat nilai dari variabel angka sama dengan 3, 
lalu lanjut ke program diluar perulangan
'''

# contoh penggunaan 2

data_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f'count = {angka}')

    if angka == data_int:
        print("nice!")
        break

    print('Hola')
'''
break akan menghentikan program perulangan saat nilai dari variabel angka sama dengan nilai
dari variabel data_int, lalu lanjut ke program diluar perulangan
'''
print('Kelar / done')
