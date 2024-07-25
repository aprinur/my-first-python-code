from . import Operasi

db_name = 'data.txt'
template = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'judul': 255*' ',
    'penulis': 255*' ',
    'tahun': 'yyyy'
}


def init_console():
    try:
        with open(db_name, 'r') as file:
            print('Database tersedia, init done!')
    except:
        print('Database tidak ditemukan, silahkan membuat file database baru')
        Operasi.create_first_data()
        # saat database tidak ada maka akan menjalankan create_first_data() dari method operasi
