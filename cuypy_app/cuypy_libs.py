def menang():
    print('SELAMAT ANDA MENANG')


def welcome(title):
    pattern = '*' * (len(title) + 6)
    print(pattern)
    print(f'** {title} **')
    print(pattern)


def nama_user():
    nama = input(' Masukkan nama anda:')  # Input nama
    while nama == '':
        nama = input('Masukkan dahulu nama anda: ')
    return nama
