
# fungsi dengan return/kembalian

"""
template fungsi dengan kembalian

def nama_fungsi(argument):
    badan fungsi
    return output

"""


# fungsi kuadrat
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat
# return berfungsi untuk mengeluarkan hasil apapun agar bisa digunakan diluar fungsi


y = kuadrat(8)  # hasi fungsi ditampung di variabel y
print(y)    # salah satu cara menampilkan hasil dari fungsi

x = 10 + kuadrat(6)
print(x)

print(kuadrat(9))   # cara menampilkan hasil dari fungsi tanpa ditampung didalam variabel


# fungsi tambah
def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2


a = fungsi_tambah(9, 7)
print(a)


# fungsi dengan return banyak
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi


k, l, m, n = operasi_matematika(90, 8)
print(f'Hasil tambah = {k}')
print(f'Hasil kurang = {l}')
print(f'Hasil kali = {m}')
print(f'Hasil bagi = {n}')

""" 
variabel k, l, m dan n digunakan untuk menampung hasil dari operasi_matematika yang direturn,
lalu ditampilkan dengan print. Jika banyaknya variabel yang digunakan untuk menampung hasil 
fungsi kurang maka akan terjadi error
"""