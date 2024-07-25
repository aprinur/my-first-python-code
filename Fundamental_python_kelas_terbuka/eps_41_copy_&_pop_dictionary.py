
# sample data
teman_teman = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
    'sep': 'asep si kasyep',
    'cuy': 'icuy curucuy'
}

# * copy dictionary

# menduplikat data tanpa copy()

teman2 = teman_teman
''' seperti pada list di eps 32, kedua variabel akan merujuk pada adress yang sama, 
sehingga apabila salah satu diubah maka akan berubah semua '''

print(f'teman teman: {teman_teman}\n')
print(f'teman2: {teman2}\n\n')


print("Mengubah value dari key 'cup'\n")
teman_teman['cup'] = 'ucup si cool'     # mengubah value dari key 'cup'
print(f'teman teman: {teman_teman}')
print(f'address: {hex(id(teman_teman))}\n')
print(f'teman2: {teman2}')
print(f'address: {hex(id(teman2))}\n\n')
'''kedua data berubah karena merujuk pada adress yang sama'''

# menduplikat data dengan copy()
friends = teman_teman.copy()
''' copy() akan menduplikat keseluruhan isi lalu memindahkan ke adress yang berbeda'''

print('menampilkan data setelah method copy()\n')
print(f'teman teman: {teman_teman}')
print(f'address: {hex(id(teman_teman))}\n')
print(f'friends: {friends}')
print(f'address: {hex(id(friends))}\n\n')

print("Mengubah value dari key 'cup'\n")
teman_teman['cup'] = 'ucuplah sang raja'    # mengubah value dari key 'cup'
print(f'teman teman: {teman_teman}\n')
print(f'friends: {friends}\n\n')
'''data pada dictionary friends tidak berubah karena terdapat pada address yang berbeda'''

# pop() dictionary
print("pop() item 'sep'\n")
data_asep = friends.pop('sep')
''' item dengan key 'sep' akan berpindah dari variabel friends ke data_asep'''

print(f'data friends : {friends}')
print(f'data asep: {data_asep}\n')

# popitem() dictionary
print("popitems()  \n")
data_terakhir = friends.popitem()
''' item terakhir akan berpindah ke variabel data_terakhir'''

print(f'data friends = {friends}')
print(f'data terakhir = {data_terakhir}\n')

'''
    copy()      = pada dictionary berfungsi untuk menduplikat data 
                  lalu memindahkannya ke address yang baru
    pop()       = pada dictionary berfungsi untuk memindahkan item(key:value) ke variabel baru 
                  berdasarkan key
    popitem()   = pada dictionary berfungsi untuk memindahkan item(key:value)
                  terakhir ke variabel baru
'''