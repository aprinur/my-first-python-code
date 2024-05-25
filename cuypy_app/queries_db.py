import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='task_to_do'
)


def tambah_kegiatan(nama_kegiatan, tempat, tanggal):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tabel_kegiatan (nama_kegiatan,tempat, tanggal) VALUES"
                   " (%s, %s, %s)",
                   (nama_kegiatan, tempat, tanggal))
    db.commit()

    if cursor.rowcount > 0:
        print('\nData berhasil dimasukkan\n')
    else:
        print('\nData gagal dimasukkan\n')


def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tabel_kegiatan")
    kegiatan = cursor.fetchall()
    if len(kegiatan) > 0:
        print('Daftar kegiatan: ')
        for task in kegiatan:
            nama_kegiatan = task[1]
            tempat_kegiatan = task[2]
            tanggal_kegiatan = task[3]
            print(f'''      
               Nama = {nama_kegiatan}
               Lokasi = {tempat_kegiatan}
               tanggal = {tanggal_kegiatan}
               ''')
    else:
        print('\nTidak ada kegiatan ')


def hapus(nama_kegiatan):
    cursor = db.cursor()
    query = 'DELETE FROM tabel_kegiatan WHERE nama_kegiatan = %s'
    try:
        cursor.execute(query, (nama_kegiatan,))
        db.commit()
        if cursor.rowcount > 0:
            print('Kegiatan berhasil dihapus')
        else:
            print('Kegiatan tidak ditemukan')
    except Error as e:
        print(f'Kegiatan gagal dihapus{e}')
    finally:
        cursor.close()

