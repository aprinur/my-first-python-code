
# tehnik menduplikasi list

a = ['Ucup', 'Otong', 'Dudung']
print(f'a = {a}')

b = a    # pass by reference
print(f'b = {b}\n\n')


# merubah nilai dari data a

a[1] = 'Michael'
b.sort()
print(f'a = {a}')
print(f'b = {b}\n\n')   # data ikut berubah


# mendapatkan address dari kedua list

print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}\n\n')


# menduplikat list dengan .copy()

print('menduplikat list dengan .copy()\n')
c = a.copy()    # full duplikat / data baru dan diletakkan di memori yang berbeda

print(f'address a = {hex(id(a))}')  # address variabel a & b sama karena
print(f'address b = {hex(id(b))}')  # terdapat pada memory yang sama.
print(f'address c = {hex(id(c))}\n')    # hasil duplikat diletakkan di memory yang berbeda

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}\n\n')

''' 
nilai dari a ataupun b akan berubah apabila salah satunya diubah, hal itu dikarenakan nilai
list a dan list b berada pada address yang sama/memory yang sama. 
untuk menduplikat nilai dari list menggunakan copy(), copy() akan membuat list dengan data 
yang sama namun dengan address yang berbeda sehingga tidak mempengaruhi list yang dicopy,
seperti data c berikut
'''
# merubah data c

print('merubah data dari index ke 0\n')
c[0] = 'Dadang'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}\n\n')

# merubah data a

print('merubah data dari index ke 1\n')
a[1] = 'Otong'

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
''' Data dari list b akan ikut berubah karena berada memory yang sama'''
