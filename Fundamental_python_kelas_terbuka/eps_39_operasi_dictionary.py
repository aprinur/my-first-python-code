# operator dictionary

data_dict = {
    'cup': 'ucup surucup',
    'tong': 'otong surotong',
    'dung': 'dudung surudung'
}

# * mencari panjang dictionary
# len pada dictionary berfungsi menampilkan jumlah pasangan key & value

lendict = len(data_dict)
print(f'panjang dari dictionary: {lendict}')

# * mengecek keberadaan suatu key didalam dict

key = 'cup'
checkkey = key in data_dict
print(f'apakah {key} ada di data_dict: {checkkey}')

# * mengakses value ( read ) dengan get
# get() hanya dipakai dalam dictionary
# get() digunakan agar saat value yang dicari tidak ada maka tidak terjadi error
print(data_dict['cup'])         # pemanggilan value tanpa get
print(data_dict.get('key'))     # pemanggilan value dengan get
print(data_dict.get('kis'))
""" apabila tidak ada value dari key yang diminta maka akan ditampilkan 'none' """
print(data_dict.get('kis', 'value tidak ditemukan'))
''' cara agar apabila value dari key yang diminta tidak ditemukan,
 maka akan messege yang ditentukan
'''

# * menambahkan dan mengupdate data
''' method update() berfungsi untuk memperbarui value apabila key sudah ada,
 dan akan menambahkan secara otomatis apabila tidak ada. 
 '''

data_dict['cup'] = 'ucup si ganteng'   # memasukkan data
print(data_dict)
data_dict['sep'] = 'asep si kasyep'     # memasukkan data
print(data_dict)

data_dict.update({'cup': 'ucup surucup'})
print(data_dict)
data_dict.update({'mal': 'malok van persie'})
print(data_dict)

# * mendelete data pada dictionary
del data_dict['mal']    # diisikan key dari value yang ingin dihapus
print(data_dict)

"""
    len() = mencari jumlah pasangan key : value dalam dictionary
    get() = mencari value dalam dictionary dan menampilkan none jika tidak ada
    update() = memperbarui value apabila key sudah ada dan akan menambahkan
               secara otomatis apabila tidak ada
"""