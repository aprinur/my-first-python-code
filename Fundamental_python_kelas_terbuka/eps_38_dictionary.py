# list -> salah satu array. Selain tuple, cara mengakses list adalah dengan menggunakan index


data_list = ['ucup', 'otong', 'dudung']
print(data_list[0])  # cara mengakses data list

# dictionary (dict) -> associative array
# untuk mengidentifikasi item didalam dict menggunakan key
# isi dari dictionary bisa boolean, string, numbers, list, termasuk dictionary

data_dict = {   # pendefinisian tipe data dictionary menggunakan kurung kurawal
    'up': 'Ucup',   # bentuk tipe data dict berupa pasangan key & value
    'tg': 'Otong',  # 'tg' = key/kunci, 'Otong' = value/nilai
    'dg': 'Dudung',  # pemisah antar item menggunakan tanda koma
    'nmbr': 2034,
    'list': data_list
}
print(data_dict['tg'])  # cara mengakses salah satu value didalam dict dengan menggunakan key
print(data_dict['nmbr'])
print(data_dict['list'])