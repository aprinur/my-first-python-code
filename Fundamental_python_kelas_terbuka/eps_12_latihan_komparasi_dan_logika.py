# latihan logika dan komparasi

# membuat gabungan area rantang dari angka

# +++++++3--------10+++++++++

inputuser = float(input('masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n: '))

# ++++++3------------
# memerikas angka kurang dari 3
iskurangdari = inputuser < 3  # menggunakan tanda kurang dari karena angka 3 tidak termasuk
print('kurang dari 3 =', iskurangdari)

# ---------------10++++++++++
# memeriksa angka lebih dari 10
islebihdari = inputuser > 10
print('lebih dari 10 =', islebihdari)

iscorrect = iskurangdari or islebihdari
print('angka yang anda masukkan =', iscorrect)


# -------3+++++++10------
# kasus irisan
print('\n', 20*'=', '\n')
inputuser = float(input('masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n: '))

# --------3++++++++
# lebih dari 3
islebihdari = inputuser > 3
print('lebih dari 3 = ', islebihdari)

# +++++++++++10---------
# kurang dari 10
iskurangdari = inputuser < 10
print('kurang dari 10 =', iskurangdari)

iscorrect = iskurangdari and islebihdari
print('angka yang anda masukkan =', iscorrect)


# pr no 1
print('\n', 30*'=', '\n')
print('''PR eps 12 nomor 1''')

# ----------0++++++++++++++5-------------8++++++++++++11--------
inputuser = float(input('masukkan angka yang bernilai'
                        '\nlebih dari 0'
                        '\ndan'
                        '\nkurang dari 5'
                        '\natau'
                        '\nlebih dari 8 '
                        '\ndan'
                        '\nkurang dari 11'
                        '\n: '))

# -----------0++++++++++
# memeriksa jika nilai lebih dari 0
islebihdari = inputuser > 0
print('lebih dari 0 =', islebihdari)

# ++++++++5-------
# memeriksa jika nilai kurang dari 5
iskurangdari = inputuser < 5
print('kurang dari 5 =', iskurangdari)

# ------8+++++++
# memeriksa jika nilai lebih dari 8
lebihdari = inputuser > 8
print('lebih dari 8 =', lebihdari)

# ++++++++11------
# memeriksa jika nilai kurang dari 11
kurangdari = inputuser < 11
print('kurang dari 11 =', kurangdari)

# hasil akhir
iscorrect = islebihdari and iskurangdari or lebihdari and kurangdari
print('angka yang anda masukkan =', iscorrect)


# pr no 2
print('\n\nPR eps 12 nomor 2')

# +++++++++++0-----------5++++++++++8----------11++++++++++
userinput = float(input('\nmasukkan nilai yang '
                        '\nkurang dari 0'
                        '\natau'
                        '\nlebih dari 5'
                        '\ndan'
                        '\nkurang dari 8'
                        '\natau'
                        '\nlebih dari 11'
                        '\n: '
                        ''))

# +++++++++0---------
# memeriksa nilai kurang dari 0
lessthan = userinput < 0
print('nilai kurang dari 0 =', lessthan)

# ----------5++++++++
# memeriksa nilai lebih dari 5
morethan = userinput > 5
print('nilai lebih dari 5 = ', morethan)

# ++++++++++8--------
# memeriksa nilai kurang dari 8
islessthan = userinput < 8
print('nilai kurang dari 8 =', islessthan)

# ----------11+++++++
# memeriksa nilai lebih dari 11
ismorethan = userinput > 11
print('nilai lebih dari 11 = ', ismorethan)

# hasil akhir
correct = lessthan or morethan and islessthan or ismorethan
print('angka yang anda masukkan =', correct)
