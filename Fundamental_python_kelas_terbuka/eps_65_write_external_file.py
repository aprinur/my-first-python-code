# 1. mode write

""" dengan menggunakan 'w' (write) maka akan secara otomatis membuat file baru jika tidak ada,
    jadi perlu memasukkan encodingnya. File akan tertimpa apabila membuka lagi file menggunakan
    statement with dengan mode 'w' (write), jadi salah satu cara mengisinya adalah dengan
    menuliskannya didalam statement 'with' yang sudah ada atau dengan mode 'a' (append) """

with open('eps_65_sample_document_1.txt', 'w', encoding='utf-8') as file:
    file.write('Marina menari diatas menara\n')


with open('eps_65_sample_document_1.txt', 'w', encoding='utf-8') as file:
    file.write('samudra diatas awan')


# program pada baris ke 8 membuat file bernama "eps_65_sample_document_1.txt" berencoding utf-8
# lalu menuliskan "Marina menari diatas menara", program berikutnya akan menimpa isinya menggunakan
# baris kode nomor 13


# 2. mode append

with open('eps_65_sample_document_2.txt', 'w', encoding='utf-8') as file:  # membuat file baru (w)
    file.write('Otong surotong')

with open('eps_65_sample_document_2.txt', 'a', encoding='utf-8') as file:  # menambahkan isinya (a)
    file.write('\nmenari diatas menara')

with open('eps_65_sample_document_2.txt', 'a', encoding='utf-8') as file:  # menambahkan isinya (a)
    file.write('\nbersama ucup surucup')

# jika file sudah ada lalu membukanya dengan mode 'a' (append), maka akan menambahkan isi file


# 3. mode r+

with open('eps_65_sample_document_3.txt', 'w', encoding='utf-8') as file:  # membuat file baru (w)
    file.write('data ke - 3\n')

with open('eps_65_sample_document_3.txt', 'r+', encoding='utf-8') as file:
    file.write('data data data\n')  # menimpa file yang sudah ada
    file.write('data selanjutnya')

with open('eps_65_sample_document_3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()  # membaca isi file
    print(data)

with open('eps_65_sample_document_3.txt', 'r+', encoding='utf-8') as file:
    file.write('data baruu banget \n')

# mode r+ digunakan untuk membuka dan menimpa karakter didalam file, jumlah karakter yang akan
# tertimpa sebanyak karakter baru yang ditambahkan