# operasi logika atau boolean

# not, or, and, xor

# NOT
print('===== NOT =====')
a = True
c = not a
print('data a =', a)
print('-------------NOT')
print('data c =', c)
print("""not berfungsi untuk membalik suatu kondisi nilai boolean""")

# OR
print('\n===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, ' =', c)
a = True
b = True
c = a or b
print(a, ' OR', b, '  =', c)
print('Jika salah satu adalah true maka hasilnya adalah true')

# AND
print('\n===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, ' =', c)
a = True
b = True
c = a and b
print(a, ' AND', b, '  =', c)
print('Hanya jika semuanya true maka akan menghasilkan true')

# XOR
print('\n===== XOR =====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, ' =', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, '  =', c)
print('Hanya jika hanya salah satu true maka hasilnya adalah true')

print('''\nBisa membandingkan lebih dari 2 nilai''')
