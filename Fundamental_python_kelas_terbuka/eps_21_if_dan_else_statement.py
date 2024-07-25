# if dan else statement

""" komposisi if statement:
1. if
2. kondisi
3. aksinya
"""

nama = input("siapa nama_global anda? : ")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline
if nama == 'ucup': print('hiiiii')
print(f'terima kasih {nama}')

# 2. program if dengan indentasi
if nama == 'ucup':
    print('kamu ganteng abieesszz')
    print('kamu juga keren banget!')
print(f'terima kasih {nama}')

# 3. else statement
if nama == 'otong':
    print('hai otooong, si keren!!!')
else:
    print("ah kamu bukan otong, kamu gak keren!!")
print('akhir dari program')
