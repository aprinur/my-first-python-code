# control flow = continue,pass, break

# pass
"""
pass = pass berfungsi sebagai dummy, jadi tidak akan dieksekusi dan lanjut ke baris berikutnya
"""

angka = 0
while angka < 5:
    angka += 1

    if angka == 3:
        pass    # ini tidak akan dieksekusi

    print(angka)

# contoh lain penggunaan pass


def contoh():
    pass    # agar fungsi bisa dipanggil dan tidak error saat dijalankan


# continue
angka = 0

print(f'angka sekarang --> {angka}')

while angka < 5:
    angka += 1
    print(f'angka sekarang --> {angka}')  # aksi 1

    if angka == 3:
        print('nice!')
        continue  # akan melanjutkan perulangan tanpa menjalankan progaram setelah continue

    print('whassup!')  # aksi 2

print('Done')

'''
dengan adanya continue maka tidak akan menjalankan program setelah continue dan melanjutkan 
perulangan
'''