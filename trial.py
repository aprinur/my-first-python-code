# import random
# import datetime
# from tkinter import ttk
# import tkinter.messagebox
#
# queue = []
# queue.copy()
# queue2 = random.randrange(1, 100)
#
# print(queue)
# print(queue2)


# x = 1
# while x <= 5:
#     print('Hallo')
#     x += 1
#
# for i in range(1, 6):
#     print('Hello world')
#

# page = tkinter.Tk()
# page.configure(background='black')
# page.geometry('300x300')
# page.title('Sample')
#
# page.mainloop()

"""ktp = {"NIK": 1234567890,
       "Nama": "Remote W. Indonesia",
       "TempatLahir": "Banyumas",
       "TanggalLahir": "10-02-1999",
       "JenisKelamin": "Laki-Laki",
       "Alamat": {"Desa": "Wisata Tanjung",
                  "RT": 4,
                  "RW": 8,
                  "Kecamatan": "Purwokerto"},
       "Agama": "Islam",
       "isMenikah": False,
       "isBekerja": True,
       "isWNI": True,
       "isValidforLife": True,
       "Hobi": ["Memancing", "Membaca", "Belajar"]
       }

ktp['Alamat']['Desa'] = 'Bandung'
print(ktp)
"""


# x = '1.5'

# try:
#     x = int(x) + 1
#     print('A')
# except TypeError:
#     print('B')
# except ValueError:
#     print('C')
# except:
#     print('D')

# x = int(x) + 1
# print(x)

# num = list(range(10))
# num = str(num)
# num.split('')
# print(num)

# a = set(input(': '))
# b = set(input(': '))
# c = set(input(': '))
# d = set(input(': '))
#
# total = b.difference(d)
# print(len(total))

# n = 1
# while n < 10:
#     print(n)
#     n += 1

# for i in range(2, 10):
#     if i % 2 == 1 or 0:
#         if not i % 3 == 1 or 0:
#             print(i)

#
# class Human:
#     def __init__(self, name: str, height: int, weight: int, gender: str,
#                  age: int):
#         """height and weight are in cm"""
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.gender = gender
#         self.age = age
#
#     def eating(self, weight: int):
#         """weight = estimation of total food weight"""
#         self.weight = self.weight + weight / 10
#         print(f"{self.name}'s weight after eating = {self.weight:.2f}")
#
#     def running(self, distance: int):
#         """distance in meter(s)"""
#         self.weight = self.weight - distance / 2000
#         print(f"{self.name}'s weight after running = {self.weight:.2f}")
#
#     def pull_up(self, count):
#         """count = count of pull up """
#         self.height = self.height + count / 100
#         print(f"{self.name}'s height after pull up = {self.height}")
#
#
# udjank = Human('Udjank', 170, 56, 'male', 34)
# mamat = Human('Mamat', 168, 55, 'male', 25)
#
# udjank.eating(1)
# udjank.running(1200)
# udjank.pull_up(9)
# print('\n')
# mamat.running(1500)
# mamat.pull_up(12)

for i in range(1, 11):
    print(i)
    for j in range(1, 6):
        print(j)
