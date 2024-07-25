
# contoh data

teman_teman = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung',
    'sep': 'asep si kasyep',
    'cuy': 'icuy curucuy'
}

# * looping untuk menampilkan key only

for teman in teman_teman:   # hanya akan menampilakan key
    print(teman)


# * operasi untuk mengambil item / iterables

# keys() method untuk mendapatkan key

keys = teman_teman.keys()   # mendapatkan key saja dari dictionary
print(keys)

for kunci in teman_teman.keys():  # mendapatkan key lalu melakukan iterasi
    print(kunci)


# values() method untuk mendapatkan value

values = teman_teman.values()   # mendapatkan value saja dari dictionary
print(values)

for value in teman_teman.values():  # mendapatkan value lalu melakukan iterasi
    print(value)


# items() method untuk mendapatkan pasangan key & value

pasangan = teman_teman.items()
print(pasangan)

for kunci, nilai in teman_teman.items():
    print(f'key = {kunci}, value = {nilai}')


# cara lain mendapatkan values lalu melakukan iterasi

for kunci in teman_teman.keys():
    print(teman_teman.get(kunci))

"""
    keys() = method untuk mendapatkan key
    values() = method untuk mendapatkan value
    items() = method untuk mendapatkan pasangan key & value
"""