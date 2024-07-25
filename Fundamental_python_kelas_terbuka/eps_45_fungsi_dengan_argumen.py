# Fungsi dengan argumen/parameter ( input)


# template fungsi adalah:
"""
def nama_fungsi(argumen/parameter):
    badan fungsi
"""


def hello_world(nama):
    """fungsi hello world menerima input. Input yang dimasukkan akan dimasukkan
       kedalam variabel"""
    print(f'Selamat datang dunia wahai {nama}')


hello_world('udcup')
hello_world('asyep')


# fungsi penjumlahan
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f'{angka1} + {angka2} = {hasil}')


tambah(23, 2)
tambah(1563, 67846)


# fungsi dengan argumen/parameter list
def hola(grup):
    data_peserta = grup.copy()
    # data dicopy agar apabila hasil copyan diubah maka tidak mempengaruhi data asli
    for peserta in data_peserta:
        print(f'Yang terhormat {peserta}')


anggota_grup = ['udcup', 'Otong', 'Dudung']

# memanggil fungsi dengan parameter list
hola(anggota_grup)
