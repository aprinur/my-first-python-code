
def calculate_circle():
    while True:
        print('\nMenghitung Luas dan keliling lingkaran\n')
        radius = float(input('Masukkan nilai radius: '))
        satuan = input("Masukkan satuan: \n")
        luas_lingkaran = 3.14 * radius ** 2
        keliling_lingkaran = 2 * 3.14 * radius

        print(f'Luas lingkaran adalah {luas_lingkaran} {satuan} dan kelilingnya adalah {keliling_lingkaran} {satuan}')

        confirm = input('Apakah akan melanjutkan kalkulasi? [y/n]: ')
        while confirm.lower() not in ['y', 'n']:
            confirm = input('Masukkan sesuai pilihan yang tersedia: ')

        if confirm.lower() == 'n':
            print('Program menghitung luas dan keliling lingkaran dihentikan')
            break
        return confirm


if __name__ == '__main__':
    calculate_circle()
