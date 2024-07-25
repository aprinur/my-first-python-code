# contoh membuat exception sendiri
from numbers import Number


# Mengecek inputan adalah angka dengan isinstance
def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        # memastikan bahwa setiap inputan adalah angka (Number)
        raise 'Input harus angka'
        # jika inputan bukan angka maka akan error dan menampilkan pesan didalam rise
    return a + b


print(tambah(5, 8))


# * Menangkap kesalahan berdasarkan tipe exception

# menangkap exception secara keseluruhan
angka = 0
# try:
#     hasil = 10 / angka
# except Exception as error_messege:
#     print(error_messege)


# menangkap exception secara spesifik
try:
    hasil = 10 / angka
except ZeroDivisionError as error_messege:
    print(error_messege)

"""
  *  Exception 
  
Definisi: Exception adalah kondisi abnormal yang terjadi selama eksekusi program yang 
          mengganggu alur normal dari instruksi program. Exception adalah jenis objek dalam
          Python yang mencakup informasi tentang kesalahan yang terjadi.
          
Kategori: Exception adalah kelas dasar dari mana semua kesalahan yang dapat ditangani diwariskan.


  *  Error 
  
Definisi: Error adalah subclass dari Exception dan menunjukkan masalah yang lebih spesifik. 
          Kesalahan bisa terjadi karena berbagai alasan, seperti masalah sintaksis, kesalahan 
          logika, atau kesalahan eksternal.
          
Kategori Utama:
    Syntax Errors: Kesalahan yang terjadi saat kode tidak mengikuti aturan sintaksis Python.
    Contoh: Kurang tanda kurung, kurang tanda petik  
    
    Runtime Errors: Kesalahan yang terjadi saat program dijalankan, meskipun sintaksisnya benar.
    Contoh: pembagian dengan nol, mengalikan number dengan string


  * Jenis jenis exception
  
ZeroDivisionError: Terjadi ketika pembagian dengan nol dilakukan.

IndexError: Terjadi ketika indeks yang tidak valid digunakan untuk mengakses elemen 
            dalam list atau tuple.
            
KeyError: Terjadi ketika kunci yang tidak valid digunakan untuk mengakses elemen dalam 
          dictionary.

TypeError: Terjadi ketika operasi atau fungsi diterapkan pada tipe data yang tidak sesuai.

ValueError: Terjadi ketika operasi atau fungsi menerima argumen yang memiliki tipe yang 
            benar tetapi nilai yang tidak valid.
            
FileNotFoundError: Terjadi ketika operasi file gagal karena file yang diminta tidak ditemukan.


  * Try and Except
  
Try and Except adalah blok dalam Python yang digunakan untuk menangani exception

template try and except:

try:
    # Blok kode yang berpotensi menimbulkan error
except ExceptionType:
    # Blok kode untuk menangani error
    
    
 - Contoh Try and Except 
  
try:
    result = 10 / 0
except ZeroDivisionError:  
    # ZeroDivisionError --> salah satu jenis exception, bisa diganti jenis yang sesuai keadaan
    print("Tidak bisa membagi dengan nol.")
    
 - Else dan Finally pada Try and Except
 
else: Dijalankan jika tidak ada exception yang terjadi.

finally: Dijalankan terlepas dari apakah exception terjadi atau tidak.


 - Contoh penggunaan Else dan Finally pada Try and Except

try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:  # FileNotFoundError --> salah satu jenis exception 
    print("File tidak ditemukan.")
else:
    print("File dibaca tanpa kesalahan.")
finally:
    file.close()
    print("File ditutup.")


"""