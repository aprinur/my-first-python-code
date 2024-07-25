# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('==== Lebih besar dari (>) ====')
hasil = a > 3
print(a, '>', 3, '=', hasil)  # True
hasil = b > 3
print(b, '>', 3, '=', hasil)  # False
hasil = b > 2
print(b, '>', 2, '=', hasil)  # False

# lebih kecil dari <
print('\n==== Lebih kecil dari (<) ====')
hasil = a < 3
print(a, '<', 3, '=', hasil)  # False
hasil = b < 3
print(b, '<', 3, '=', hasil)  # True
hasil = b < 2
print(b, '<', 2, '=', hasil)  # False

# lebih besar dari atau sama dengan >=
print('\n==== Lebih besar dari atau sama dengan (>=) ====')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)  # True
hasil = b >= 3
print(b, '>=', 3, '=', hasil)  # False
hasil = b >= 2
print(b, '>=', 2, '=', hasil)  # True

# lebih kecil dari atau sama dengan <=
print('\n==== Lebih kecil dari atau sama dengan (<=) ====')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)  # False
hasil = b <= 3
print(b, '<=', 3, '=', hasil)  # True
hasil = b <= 2
print(b, '<=', 2, '=', hasil)  # True

# Sama dengan (==)
print('\n====  sama dengan (==) ====')
hasil = a == 4
print(a, '==', 4, '=', hasil)  # True
hasil = b == 4
print(b, '==', 4, '=', hasil)  # False
""" ( = ) adalah assignment. (==) adalah sama dengan, digunakan untuk membandingkan nilai
    disisi kiri dengan sisi kanan   """
# Tidak Sama dengan (!=)
print('\n====  sama dengan (!=) ====')
hasil = a != 4
print(a, '!=', 4, '=', hasil)  # False
hasil = b != 4
print(b, '!=', 4, '=', hasil)  # True


print('\n====  Object identity (is) ====')
# 'is' sebagai komparasi object identity
# 'is' tidak disarankan untuk membandingkan nilai yang tidak dimasukkan ke variabel (literal)
# 'is' memeriksa apakah dua variabel merujuk pada objek yang sama didalam memori
x = 5  # contoh assignment membuat object
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print(' x is y =', hasil)
# hasilnya true karena nilai dari x dan y berada pada memori yang sama

x = 5  # contoh assignment membuat object
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print(' x is y =', hasil)
# hasilnya false karena nilai dari x dan y tidak berada pada memori yang sama


print('\n====  Object identity (is not) ====')
# 'is not' sebagai komparasi object identity
# 'is not ' tidak disarankan untuk membandingkan nilai yang tidak dimasukkan ke variabel(literal)
# 'is not' memeriksa apakah dua variabel tidak merujuk pada objek yang sama di memori
x = 5  # contoh assignment membuat object
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print(' x is y =', hasil)
# hasilnya false karena nilai dari x dan y berada pada memori yang sama

x = 5  # contoh assignment membuat object
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print(' x is y =', hasil)
# hasilnya true karena nilai dari x dan y tidak berada pada memori yang sama

print('''
    - object identity 'is' memeriksa apakah dua variabel merujuk pada objek yang sama di memori
    
    - object identity 'is not' memeriksa apakah dua variabel tidak merujuk pada objek yang sama
    
    - comparation '==' memeriksa kesamaan nilai yang dibandingkan
''')
