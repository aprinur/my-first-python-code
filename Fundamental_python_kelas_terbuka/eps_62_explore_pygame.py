
import pygame

""" Pygame adalah library python untuk membuat game"""
""" 
Struktur dalam game adalah :

- Init ( map, karakter )
- User input, database input ( inputan dari user)
- update asset 
- render ke dispaly
"""

# * Init
''' init berfungsi menginisialisiasi game '''
pygame.init()  # berfungsi menjalankan game engine

# variable running game
isrun = True  # berfungsi menjaga agar aplikasi berjalan

# membuat display surface object
'''membuat window untuk area permainan. Untuk menjalankannya memerlukan 
   pygame.display.update()'''
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# parameter object game
# posisi object
x = 250
y = 250

# ukuran object
panjang = 10
lebar = 10

# kecepatan gerak
speed = 0.1


while isrun:  # jika tidak ada keterangan False maka secara otomatis True
    # pygame.time.delay(50)  <-- memberikan delay saat menekan kontrol
    # * user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrun = False

    keys = pygame.key.get_pressed()  # mengambil semua inputan keyboard press
    """Posisi X0 & Y0 berada di pojok kiri atas"""
    if keys[pygame.K_LEFT] and x > 0:  # input arrow kiri
        x -= speed

    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:  # input arrow kanan
        x += speed

    if keys[pygame.K_UP] and y > 0:  # input arrow atas
        y -= speed

    if keys[pygame.K_DOWN] and y < window_panjang - panjang:  # input arrow bawah
        y += speed
    '''elif dan else tidak digunakan agar bisa menekan lebih dari 1 key bersamaan'''

    # * update asset
    window.fill((255, 255, 255))  # merubah warna latar menjadi putih
    pygame.draw.rect(window, (0, 255, 0), (x, y, lebar, panjang))
    ''' membuat object segiempat untuk dimainkan. window = area yang digunakan, 
        (255, 0, 0) = warna merah (R, G, B), (x, y, lebar, panjang) = ukuran dan posisi '''
    # * render ke display
    pygame.display.update()
pygame.quit()
