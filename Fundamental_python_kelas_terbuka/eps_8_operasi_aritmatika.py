""" Operasi Aritmatika"""

a = 10
b = 3
# mendukung bilangan negatif (-)

# Operasi penjumlahan +
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)  # Akan otomatis dirubah ke float apabila hasil desimal

# Operasi eksponen ( pangkat ) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi modulus ( sisa bagi ) %
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi floor division ( dibulatkan kebawah ) //
hasil = a // b
print(a, '//', b, '=', hasil)


""" prioritas operasi, operational precedence"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

# urutan yang akan dikalkulasi adalah:
# 1. ( )
# 2. eksponen / perpangkatan ( ** )
# 3. perkalian, pembagian, floor division, modulus ( * , / , // , % )
# 4. pertambahan, pengurangan ( + , - )

