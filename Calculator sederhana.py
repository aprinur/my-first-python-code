def penjumlahan(a, b):
    jumlah = a + b
    print(f'Hasil dari {a} ditambah {b} adalah {jumlah}')
    return jumlah


def pengurangan(a, b):
    kurang = a-b
    print(f'Hasil dari {a} dikurang {b} adalah {kurang}')
    return kurang


def perkalian(a, b):
    kali = a*b
    print(f'Hasil dari {a} dikali {b} adalah {kali}')
    return kali


def pembagian(a, b):
    bagi = a/b
    print(f'Hasil dari {a} dibagi {b} adalah {bagi}')
    return bagi


angka_a = float(input('Masukkan angka untuk kalkulasi :'))
angka_b = float(input('Masukkan angka selanjutnya :'))


def menu():

    while True:
        print('pilih operasi yang akan dilakukan:')
        print('1. Penjumlahan')
        print('2. Pengurangan')
        print('3. Perkalian')
        print('4. Pembagian')
        print('5. OUT')

        opsi = input('Masukkan angka yang dipilih: ')

        if opsi == '1':
            penjumlahan(a=angka_a, b=angka_b)
        elif opsi == '2':
            pengurangan(a=angka_a, b=angka_b)
        elif opsi == '3':
            perkalian(a=angka_a, b=angka_b)
        elif opsi == '4':
            pembagian(a=angka_a, b=angka_b)
        elif opsi == '5':
            print('Sesi telah selesai')
            break
        else:
            print('Opsi tidak valid')


if __name__ == '__main__':
    menu()
