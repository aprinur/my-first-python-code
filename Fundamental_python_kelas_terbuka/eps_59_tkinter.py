# Membuat GUI dengan tkinter
# GUI --> Graphical User Interface

import tkinter as tk  # mengimport tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()  # membuat objek bernama window
window.configure(bg='white')  # mengubah background menjadi putih
window.geometry('500x500')
window.resizable(False, False)
window.title('Do Nothing App')

#  Variabel dan Fungsi
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()


def tombol_click():
    """fungsi ini dipanggil oleh tombol"""
    pesan = f'Halo {nama_depan.get()} {nama_belakang.get()}, Apa kabar?'
    # .get() berfungsi mengambil nilai dari variabel
    showinfo(title='Notice', message=pesan)


# Frame Input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# Komponen - komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text='Nama Depan')
nama_depan_label.pack(padx=10, pady=10, fill='x', expand=True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
nama_depan_entry.pack(padx=10, pady=10, fill='x', expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text='Nama Belakang')
nama_belakang_label.pack(padx=10, pady=10, fill='x', expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
nama_belakang_entry.pack(padx=10, pady=10, fill='x', expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text='Sapa!', command=tombol_click)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)

# Main loop window
window.mainloop()