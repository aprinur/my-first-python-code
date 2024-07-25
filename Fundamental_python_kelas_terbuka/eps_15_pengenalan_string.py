data = 'ini adalah string'
print(data)
print(type(data))  # cara melakukan pengecekan tipe data

# *  Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo, apa kabar?"')  # quote pembuka dan penutup harus sama
print("'Hallo, apa kabar?'")
print("ini adalh hari jum'at")  # double quote digunakan jika dalam string ada
# karakter single  quote

# *  Menggunakan tanda \

# membuat tanda single quote ( ' ) menjadi string dengan backslash  ( \ )
print('mari shalat jum\'at')
print('g\'day, isn\'t it ?')

# Backslash
print("C:\\user\\ucup")  # contoh dalam penulisan folder

# tab
print("ucup\t\totong,")  # menggunakan \t sebagai tab

# backspace
print("ucup \botong")  # menggunakan \b sebagai backspace ( menghapus 1 karakter sebelumnya )

# newline
print("baris pertama.\nbaris kedua")  # LF -> line feed -> digunakan oleh unix, macos, linux
print("baris pertama.\rbaris kedua")  # CR -> carriage return -> dipakai oleh commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua")  # CRLF -> line feed carriage return -> dipakai windows

# * Menggunakan string literal atau raw

print('C:\new folder')  # akan salah pathnya karena tidak ada huruf n

# menggunakan raw string
print(r'C:\new folder')  # setiap karakter akan dicetak dengan menambahkan huruf r didepan tanda petik

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")