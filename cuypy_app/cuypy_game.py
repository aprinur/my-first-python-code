import random
from cuypy_libs import menang
from cuypy_libs import nama_user


def start():
    while True:
        cuypy_position = random.randrange(1, 5)
        bentuk_goa = '(_)'  # Membuat bentuk goa
        goa_kosong = [bentuk_goa] * 4  # Membuat bentuk goa menjadi 4
        goa_isi = goa_kosong.copy()  # Fungsi .copy() agar variabel goa kosong tidak terdampak program selanjutnya

        goa_isi[cuypy_position - 1] = '(0_0)'

        goa_kosong = ' '.join(goa_kosong)  # Menghilangkan tanda petik, kurung siku dan koma
        goa_isi = ' '.join(goa_isi)  # Menghilangkan tanda petik, kurung siku dan koma

        print(f' Halo {nama_user()}, perhatikan goa dibawah ini \n\n{goa_kosong}\n')

        pilihan_user = input(' Ada dimanakah CUYPY berada? [1/2/3/4]: ')  # Input pilihan user

        if not pilihan_user.isdigit() or int(pilihan_user) not in [1, 2, 3, 4]:  # Validasi pilihan agar hanya
            # antara 1 sampai 4
            print(' Opsi tidak valid')
            break
        else:
            pilihan_user = int(pilihan_user)
            if pilihan_user == cuypy_position:  # Bila jawaban benar
                print(f''' \n {menang()}, CUYPY berada pada nomor {cuypy_position} \n {goa_isi} ''')
            else:  # Bila jawaban salah
                print(f'''\n Maaf kamu kalah, CUYPY berada pada nomor {cuypy_position} \n {goa_isi}''')
            konfirmasi_lanjut = input('Apakah akan melanjutkan game [y/n]: ')
            if konfirmasi_lanjut.lower() == 'n':
                print('Permainan telah usai')
                break


if __name__ == '__main__':
    start()
