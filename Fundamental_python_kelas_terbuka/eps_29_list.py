# LIST

# list = kumpulan data

# * bentuk bentuk list

# list data numbers
data_angka = [1, 5, 7, 2, 3]
print(data_angka)   # data akan ditampilkan sesuai urutan pada list yang ada

# list data string
data_string = ['ucup', 'otong', 'odah']
print(data_string)

# list data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# list data campuran
data_campuran = ['bla-bla', 2, 'ireng', 'ucup', True, 'otong', False]
print(data_campuran)


# * cara cara membuat list

# dengan range
data_range = range(0, 10)  # range dari 0 sampai 10 - 1
print(data_range)
data_list = list(data_range)    # casting dari range menjadi list
print(data_list)
print(list(range(10, 25)))

# dengan range dan increment
data_range = range(0, 10, 2)  # range(start, stop, step) dipisahkan dengan koma
print(data_range)
data_list = list(data_range)    # casting dari range menjadi list
print(data_list)
print(list(range(10, 25, 2)))

# membuat list dengan for loop, list comprehension
list_dengan_for = [i for i in range(0, 10)]
print(list_dengan_for)

# membuat list dengan for loop, list comprehension dan hasil berpangkat
list_dengan_for = [i ** 2 for i in range(0, 10)]
print(list_dengan_for)

# membuat list dengan for dan if
list_for_if = [i for i in range(0, 10) if i != 5]
# akan menampilkan semua angka dari 0 sampai 9 kecuali angka 5
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 == 0]
# akan menampilkan angka yang genap saja
print(list_for_if)
