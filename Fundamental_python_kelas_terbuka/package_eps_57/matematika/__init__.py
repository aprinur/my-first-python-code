# Mengimport module dari package 'matematika'

from . import basic
from . import scientific

# mengimport fungsi didalam module

from .basic import kali, tambah
from .scientific import pangkat