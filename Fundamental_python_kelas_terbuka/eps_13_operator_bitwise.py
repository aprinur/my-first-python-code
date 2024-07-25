# operator bitwise/ operator binary/ biner
"""
bitwise = operasi masing masing bit
cara penggunaan operator bitwise sama dengan operator logika dan boolean
karena pada dasarnya memang diperuntukkan untuk bitwise bukan untuk boolean

penjelasan bit dan hitungannya:
yaitu unit dasar dari data dalam komputasi dan komunikasi digital.
Sebuah bit dapat memiliki salah satu dari dua nilai, yaitu 0 atau 1
cara mendapatkan nilai integer dari binary adalah dengan angka 2 dipangkatkan posisi indexnya
contoh:
    int 2 = 00000010
            ||||||||
            vvvvvvvv
no index  = 76543210 = angka 1 berada pada index ke 1,
                       jadi nilai 2 dipangkatkan 1 sehingga bernilai 2
    int 1 = 00000001
            ||||||||
            vvvvvvvv
no index  = 76543210 = angka 1 berada pada index ke 0,
                        jadi nilai 2 dipangkatkan 0 sehingga bernilai 1
    int _ = 00001001
            ||||||||
            vvvvvvvv
no index  = 76543210 =  angka 1 berada pada index ke 0 serta index ke 3,
                        jadi nilai 2 dipangkatkan 0, juga nilai 2 dipangkatkan 3,
                        lalu hasilnya dijumlahkan.
                        2**0 = 1
                        2**3 = 8
                        1 + 8 = 9
                        jadi 00001001 = adalah integer 9

Angka 2 berasal dari basis sistem bilangan biner, yang hanya menggunakan dua digit (0 dan 1)

"""

# operator bitwise = or, and, xor, not
a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n==========OR==========')
print('nilai :', a, 'binary : ', format(a, '08b'))
print('nilai :', b, 'binary : ', format(b, '08b'))
print('---------------------------------------(|)')
print('nilai :', c, 'binary : ', format(c, '08b'))

# bitwise  AND (&)
c = a & b
print('\n==========AND==========')
print('nilai :', a, 'binary : ', format(a, '08b'))
print('nilai :', b, 'binary : ', format(b, '08b'))
print('---------------------------------------(|)')
print('nilai :', c, 'binary : ', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n==========XOR==========')
print('nilai :', a, 'binary : ', format(a, '08b'))
print('nilai :', b, 'binary : ', format(b, '08b'))
print('---------------------------------------(^)')
print('nilai :', c, 'binary : ', format(c, '08b'))

# bitwise NOT (~)
c = ~ a
print('\n==========NOT==========')
print('nilai :', a, 'binary : ', format(a, '08b'))  # output = 9
print('---------------------------------------(~)')
print('nilai :', c, 'binary : ', format(c, '08b'))  # output = -10
"""
hasil dari operasi diatas lebih 1 angka yaitu -10 dikarenakan 
operasi bitwise NOT di Python melibatkan representasi bilangan dalam bentuk two's complement 
untuk bilangan negatif. Dalam two's complement, membalik semua bit dan menambahkan 1 akan 
menghasilkan nilai negatif dari bilangan asli ditambah 1.
Hasil dari bitwise NOT pada bilangan positif dalam Python adalah bilangan negatif, 
karena Python menggunakan representasi two's complement.
Two's complement adalah metode untuk merepresentasikan bilangan
bulat bertanda (positif dan negatif) dalam sistem biner.
( chatgpt )
"""

"""
-10  -9  -8  -7  -6  -5  -4  -3  -2  -1 | 0  1  2  3  4  5  6  7  8 9 
                                        |
                                        v
                         mirroring dimulai dari tanda tersebut 
        jadi jika nilainya adalah 9 saat dilakukan operasi not akan menjadi -10
"""

# cara untuk membalik angka 0 menjadi 1 seperti pada one's complement bisa dengan XOR
# contoh:
print('---------------------------------------(^)')
c = ~ b
d = 0b0000001001
e = 0b1111111111
print('nilai :', e ^ d, ', binary :', format(e ^ d, '08b'))
print('---------------------------------------(~)')
print('Nilai c:', c, ' binary:', format(c & 0xFF, '08b'))
'''bisa juga menggunakan '& 0xFF' untuk 
merubah ke one'complement '''

# shifting

# shift right ( >> )
''' berfungsi menggeser nilai kekanan sesuai nilai yang dimasukkan 
    bisa juga disebut menambahkan nilai nol diujung kiri dan menghapus nilai  
    yang ada diujung kanan '''
c = a >> 2  # kode biner digeser 2 angka kekanan
print('\n========== >> ==========')
print('nilai :', a, 'binary : ', format(a, '08b'))
print('---------------------------------------(>>)')
print('nilai :', c, 'binary : ', format(c, '08b'))

# shift left ( << )
''' berfungsi menggeser nilai kekiri sesuai nilai yang dimasukkan
    bisa juga disebut menambahkan nilai nol diujung kanan dan menghapus nilai  
    yang ada diujung kiri'''
c = a << 2  # kode biner digeser kekiri dua angka
print('\n========== >> ==========')
print('nilai :', a, 'binary : ', format(a, '08b'))
print('---------------------------------------(<<)')
print('nilai :', c, 'binary : ', format(c, '08b'))