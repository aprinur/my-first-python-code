
from eps_55_module_matematika import tambah as add
from eps_55_module_matematika import kali as mul
from eps_55_module_matematika import pangkat as exp

'''cara lain penulisan alias :

    from eps_55_module_matematika import tambah as add, kali as mul, pangkat as exp

tambah, kali dan pangkat adalah fungsi yang ada didalam module eps_55_module_matematika
'''

""" 
as atau alias digunakan untuk mengganti nama fungsi, namun hanya berlaku pada program yang 
nama fungsinya diganti diprogram tersebut    
"""

''' 
    contoh lain penggunaan as/alias:

from eps_55_module_matematika as math
'''

hasil_tambah = add(1, 3, 4, 6, 7, 8)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = mul(2, 5, 1, 6, 4)
print(f'hasil kali = {hasil_kali}')

pangkat_3 = exp(3)
print(f'hasil pangkat 3 = {pangkat_3(3)}')