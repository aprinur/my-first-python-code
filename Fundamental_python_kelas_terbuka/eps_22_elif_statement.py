# elif = else if statement


"""
format penulisan if-elif-else:

if kondisi:
    aksi true
elif kondisi:
    aksi true
elif kondisi:
    aksi true
else:
    aksi

tidak ada batasan dalam penggunaan elif
"""

nama = input("Masukkan nama_global anda : ")
if nama == 'ucup':  # kondisi 1
    print("Hola ucup!! guten moregen")  # aksi true 1
elif nama == "otong":  # kondisi 2
    print("konichiwa otong")  # aksi true 2
elif nama == 'mario':  # kondisi 3
    print("Halo mario")  # aksi true 3
else:
    print("ANDA SIAPA ??")  # aksi false
print('ini adalah akhir dari program')