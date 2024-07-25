# method ini sebagi backend

import os
from time import time
from .util import random_string
from . import Database
import time


def delete(no_buku):
    try:
        with open(Database.db_name, 'r') as file:
            counter = 0

            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku-1:
                    pass
                else:
                    with open('data_temp.txt', 'a', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print('database error')

    os.rename('data_temp.txt', Database.db_name)


def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.template.copy()

    # memasukkan parameter ke template
    data['pk'] = pk
    data['date_add'] = data_add
    data['penulis'] = penulis + Database.template['penulis'][len(penulis):]
    data['judul'] = judul + Database.template['judul'][len(judul):]
    data['tahun'] = str(tahun)

    # memposisikan data baru sebelum dimasukkan ke database
    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"

    panjang_data = len(data_str)

    # memindahkan kursor ke nomor yang sudah dipilih user dengan fungsi seek lalu menuliskannya ke database
    try:
        with open(Database.db_name, 'r+', encoding='utf-8') as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print('error dalam update data')


def create(tahun, judul, penulis):
    data = Database.template.copy()  # mengcopy template

    # memasukkan data ke template yang sudah dibuat
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['penulis'] = penulis + Database.template['penulis'][len(penulis):]
    data['judul'] = judul + Database.template['judul'][len(judul):]
    data['tahun'] = str(tahun)

    # memposisikan data untuk diinput ke database
    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"

    # menambahkan data yang sudah dibuat ke database
    try:
        with open(Database.db_name, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Gagal maning')


def create_first_data():
    # meminta judul, nama penulis, dan tahun dari user
    penulis = input('Penulis: ')
    judul = input('Judul: ')
    # tahun dibuat agar selalu 4 digit
    while True:
        try:
            tahun = int(input('Tahun\t: '))
            if len(str(tahun)) == 4:
                break
            else:
                print('Tahun harus 4 digit (yyyy) dan angka,silahkan masukkan tahun lagi')

        except:
            print('Tahun harus 4 digit (yyyy) dan angka, silahkan masukkan tahun lagi')

    data = Database.template.copy()  # mengcopy template database dari method database
    '''template dicopy agar template asli tidak berubah apabila digunakan di program lain'''

    # menjalankan fungsi random_string untuk mendapatkan string acak sebagai pk
    data['pk'] = random_string(6)

    # mendapatkan waktu aktual saat database dibuat
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z ', time.gmtime())

    # memasukkan nilai dari variabel 'penulis' ke template yang telah dibuat dan sisanya diisi spasi
    data['penulis'] = penulis + Database.template['penulis'][len(penulis):]

    # memasukkan nilai dari variabel 'judul' ke template yang telah dibuat dan sisanya diisi spasi
    data['judul'] = judul + Database.template['judul'][len(judul):]

    # memasukkan nilai variabel 'tahun' ke template tahun
    data['tahun'] = str(tahun)

    # memposisikan data sebelum dimasukkan ke database
    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"

    try:
        with open(Database.db_name, 'w', encoding='utf-8') as file:  # membuat database baru
            file.write(data_str)  # memasukkan 'data_str' ke database
    except:
        print('Gagal')


def read(**kwargs):
    try:
        # membuka nilai dari db_name dengan mode baca
        with open(Database.db_name, 'r') as file:
            # menghitung banyaknya data didalam db_name
            content = file.readlines()
            jumlah_buku = len(content)

            # mengecek apabila database memiliki isi
            if 'index' in kwargs:
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('Membaca database error')
        return False