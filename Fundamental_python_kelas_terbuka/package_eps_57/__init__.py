# Mengimport keseluruhan module
from . import matematika
from . import phisika

"""
    Penambahan module 'phisika' pada file '__init__.py' bertujuan agar pada saat  
file utama mengimport package, module akan diimport secara otomatis, sedangkan 'matematika'
pada program diatas merujuk pada package 'matematika' yang ada didalam 'package_eps_57'. 
"""

# Mengimport fungsi tertentu dalam module
'''Hal ini berfungi untuk mempersingkat penulisan kode dan untuk penggunaan fungsi spesifik 
dari suatu module'''
from .phisika import gaya  # Mengimport fungsi 'kali' dari module 'matematika'

# mengimport method dengan keyword __all__

# __all__ = [  # tidak disarankan untuk dipakai
#     'matematika',
#     'phisika'
# ]