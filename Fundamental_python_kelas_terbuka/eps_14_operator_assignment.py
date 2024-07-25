# operasi yand dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment
print('\nAssignment operator')
a = 5  # adalah assignment
print('nilai a =', a)

print('\nAddition Assignment')
a += 1  # artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi', a)

print('\nSubtraction Assignment')
a -= 1  # artinya adalah a = a - 1
print('nilai a -= 1, nilai a menjadi', a)

print('\nMultiplication Assignment')
a *= 1  # artinya adalah a = a * 1
print('nilai a *= 1, nilai a menjadi', a)

print('\nSubtraction Assignment')
a /= 1  # artinya adalah a = a / 1
print('nilai a /= 1, nilai a menjadi', a)

b = 10
print('\nnilai b =', b)

print('\nRemainder Assignment')
b %= 3  # artinya adalah b = b % 3
print('nilai b %= 3, nilai b menjadi', b)

b = 10
print('\nnilai b =', b)

print('\nFloor division Assignment')
b //= 3  # artinya adalah b = b // 3
print('nilai b //= 3, nilai b menjadi', b)

a = 5
print('\nnilai a =', a)

print('\nExponent Assignment')
a **= 3  # artinya adalah a = a * 3
print('nilai a **= 3, nilai a menjadi', a)


# operasi bitwise.
# Bitwise OR ( | )
print('\nBitwise OR ( | )')
c = True
print('\nnilai c = ', c)
c |= False
print('nilai c |= False, nilai c menjadi', c)
c = False
print('\nnilai c = ', c)
c |= False
print('nilai c |= False, nilai c menjadi', c)

# Bitwise AND ( & )
print('\nBitwise AND ( & )')
c = True
print('\nnilai c = ', c)
c &= False
print('nilai c &= False, nilai c menjadi', c)
c = True
print('\nnilai c = ', c)
c &= True
print('nilai c &= True, nilai c menjadi', c)

# Bitwise XOR ( ^ )
print('\nBitwise AND ( ^ )')
c = True
print('\nnilai c = ', c)
c ^= False
print('nilai c ^= False, nilai c menjadi', c)
c = True
print('\nnilai c = ', c)
c ^= True
print('nilai c ^= True, nilai c menjadi', c)

# Shifting
print('\nSHIFTING  ( << , >> )')
d = 0b0100
print('\nnilai d =', format(d, '04b'))
# Right shift >>
print('\nRight shift  ( >> )')
d >>= 2
print('nilai d >>= 2, nilai d menjadi', format(d, '04b'))
# Left shift
print('\nLeft shift  ( << )')
d <<= 1
print('nilai d <<= 1, nilai d menjadi', format(d, '04b'))
'''
Penggeseran berdasarkan nilai terakhir disuatu variabel
'''