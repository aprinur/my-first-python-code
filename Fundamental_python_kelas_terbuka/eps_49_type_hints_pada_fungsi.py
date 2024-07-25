# type hints untuk fungsi
"""
   Type hints berfungsi untuk memberikan petunjuk apa yang harus diisikan dalam parameter agar
    sesuai dengan tujuan pembuatan fungsi
"""

# contoh bentuk standar fungsi yang sudah dipelajari
"""
def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi('udcup')
fungsi(True)

 program akan berjalan normal karena print bisa menampilkan semua tipe data
 namun apabila tujuan fungsinya diubah seperti berikut akan terjadi eror. 
    
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil)

fungsi(1)
fungsi('udcup')
fungsi(True)

error terjadi karena tipe data string tidak bisa dikuadratkan, oleh karena itu type hints digunakan
untuk memberi petunjuk tipe data apa yang dimasukkan kedalam parameter
"""


# contoh penggunaan type hints
def pangkat(argumen: int):
    # : int berfungsi sebagai penanda apabila nilai dari argumen harus integer
    output = argumen ** 3
    return output


print(pangkat(3))


def exponen(argumen: int) -> int:
    """
    : int berfungsi sebagai penanda apabila nilai dari argumen harus integer
    -> int berfungsi penanda apabila hasil dari fungsi adalah integer
    """
    hasil = argumen ** 2
    return hasil


print(exponen(4))

''' type hints bisa berisi tipe data apapun agar parameter/argumen 
    sesuai dengan tujuan pembuatan fungsi. 
    contoh = :int, :str, :bool ; 
    
    contoh penanda hasil keluaran/return fungsi = -> int, -> str, -> bool  
'''