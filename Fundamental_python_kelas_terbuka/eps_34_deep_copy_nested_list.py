
data_0 = [1, 2]
data_1 = [3, 4]

data_2d = [data_0, data_1, 9, 10]
data_2d_copy = data_2d.copy()

print(f'data = {data_2d}')
print(f'data copy = {data_2d_copy}')


# * mengambil data dari nested list

print(f'\nseluruh data didalam list = {data_2d}')

data = data_2d[0]   # untuk mengambil seluruh data list pertama dari nested list
print(f'list pertama didalam nested list = {data}')

data = data_2d[0][0]    # untuk mengambil data pertama dari list pertama
# yang berada didalam nested list.
print(f'data pertama dari list pertama didalam nested list  = {data}')

data = data_2d[1][0]  # untuk mengambil data pertama dari list kedua
# yang berada didalam nested list.
print(f'data pertama dari list kedua didalam nested list  = {data}')


# * menampilkan address data_2d dan address data_2d_copy

print(f'\naddress data_2d = {hex(id(data_2d))}')
print(f'address data_2d_copy = {hex(id(data_2d_copy))}')

# menampilkan address data pertama list pertama data_2d dan data_2d_copy
print(f'address dari data pertama dari list pertama '
      f'didalam nested list data_2d = {hex(id(data_2d[0]))}')
print(f'address dari data pertama dari list pertama '
      f'didalam nested list data_2d_copy = {hex(id(data_2d_copy[0]))}')

data_2d[1][0] = 5   # mengubah data pertama dari list kedua didalam nested list
data_2d[2] = 50  # mengubah data ketiga dari nested list (urutan ketiga dalam data_2d bukan list)

print(f'\ndata = {data_2d}')
print(f'data copy = {data_2d_copy}')
# karena urutan ketiga dalam data_2d bukan list maka data duplikat tidak berubah


# * penggunaan deepcopy untuk menyalin nilai dari nested loop

from copy import deepcopy  # fungsi untuk melakukan duplikasi nilai list didalam nested list

data_2d = [data_0, data_1, 9, 10]
data_2d_deepcopy = deepcopy(data_2d)      # cara penggunaan deepcopy

# menampilkan address data_2d dan address data_2d_deepcopy
print(f'\naddress asli = {hex(id(data_2d))}')
print(f'address deepcopy = {hex(id(data_2d_deepcopy))}')

print(f'address dari data pertama dari list pertama '
      f'didalam nested list data_2d = {hex(id(data_2d[0]))}')
print(f'address dari data pertama dari list pertama '
      f'didalam nested list data_2d_deepcopy = {hex(id(data_2d_deepcopy[0]))}')
'''
 adress dari setiap data didalam list akan mengalami perubahan karena deepcopy akan menduplikat
 nilai dari list dan memindahkannya kedalam address yang baru
 '''

data_2d[1][0] = 99
print(f'\ndata = {data_2d}')
print(f'data copy = {data_2d_copy}')
print(f'data copy = {data_2d_deepcopy}')
''' saat dilakukan perubahan data pada nested list data_2d maka nested list data_2d_copy akan ikut
 berubah karena masih berada pada address yang sama, namun tidak demikian dengan data_2d_deepcopy
 karena setiap data dalam nested list data_2d_deepcopy berada pada address yang berbeda'''