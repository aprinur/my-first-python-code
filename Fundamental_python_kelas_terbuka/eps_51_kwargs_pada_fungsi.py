# **kwargs
# **kwargs = keyword args


# fungsi tanpa **kwargs
def fungsi(nama, tinggi, berat):
    """ fungsi biasa"""
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')


fungsi('ucup', 189, 80)


# penggunaan **kwargs
def fungsi(**kwargs):
    print(kwargs)   # saat ditampilkan akan menjadi tipe data dictionary
    print(kwargs['nama'])   # menampilkan value berdasarkan key
    nama = kwargs['nama']   # memasukkan value dari keyword 'nama' ke variabel 'nama'
    tinggi = kwargs['tinggi']  # memasukkan value dari keyword 'tinggi' ke variabel 'tinggi'
    berat = kwargs['berat']  # memasukkan value dari keyword 'berat' ke variabel 'berat'
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')
    # karena tipe data diubah menjadi dictionary maka bisa diambil valuenya berdasarkan key


fungsi(nama='ucup', tinggi=189, berat=80)
# parameter **kwargs memerlukan pendefinisian keyword untuk setiap nilai yang akan dimasukkan
# kedalam fungsi, pada kode diatas nama= adalah keyword, begitu juga dengan tinggi=, dan berat=


# contoh penggunaan *args dan **kwargs
def math(*args, **kwargs):
    output = 0
    if kwargs['option'] == 'tambah':
        for angka in args:
            output += angka
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    else:
        print('tidak ada operasi')

    return output


hasil = math(1, 2, 3, 4, option='tambah')
print(f'hasil jumlah = {hasil}')
hasil = math(1, 2, 3, 4, option='kali')
print(f'hasil kali = {hasil}')
print(f'hasil kali = {math(1, 2, 3, 4, 5, option='kali')}')

'''
    karena dalam fungsi math di atas terdapat parameter *args dan **kwargs maka secara otomatis 
    option= akan diproses sebagai keyword dalam **kwargs dan nilai didepan keyword akan diproses
    dalam *args. Pendefinisian keyword dalam **kwargs cukup menggunakan key lalu diikuti '='.
    contoh: option= , bilangan=, kata= , dll
'''
