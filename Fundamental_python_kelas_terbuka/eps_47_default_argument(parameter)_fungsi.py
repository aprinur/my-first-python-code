# Default argument

"""
   - template fungsi dengan argumen/parameter:

    def fungsi(argumen):
        badan fungsi



   - template fungsi dengan default argumen:

    def fungsi(argumen=nilai defaultnya):
        badan fungsi

"""


# * contoh fungsi dengan argumen
def say_hello(nama):
    print(f'hallo {nama}')


# pemanggilan fungsi
say_hello('udcup')  # jika parameter tidak memiliki nilai default, parameter/argumen harus diisi


def eksponen(angka, pangkat):
    hasil = angka ** pangkat
    return hasil


# pemanggilan fungsi
print(eksponen(pangkat=3, angka=4))
# penulisan parameter bisa dibalik namun harus ditulis semua jika tidak memiliki nilai default


# * contoh fungsi dengan default argumen

def sapa(nama='kamu'):
    print(f'Hai {nama}')


# pemanggilan fungsi
sapa('udjang')
sapa()
''' 
    apabila parameter pada fungsi yang memiliki nilai default tidak diisi maka tidak akan error 
    karena akan secara otomatis menampilkan nilai default parameter
'''


# * fungsi dengan mulitple parameter"""
# contoh 1
def sapa_dia(nama, pesan='apa kabar??'):
    print(f'Hai {nama}, {pesan}')


"""
    pada fungsi diatas parameter nama_global tidak memiliki nilai default jadi harus diisi,
    sedangkan parameter pesan memiliki nilai default sehingga apabila tidak diisi maka akan
    menampilkan nilai default dari parameter namun akan menampilkan nilai inputan user apabila
    diisi
"""

# pemanggilan fungsi
sapa_dia('udcup', 'kamu lagi apa')


# contoh 2
def banyak(angka_1=1, angka_2=2, angka_3=3, angka_4=4):
    hasil = angka_1 + angka_2 + angka_3 + angka_4
    return hasil


print(banyak())
print(banyak(angka_3=90, angka_1=45))
# parameter bisa digunakan sebagian dengan penulisan tidak sesuai urutan
