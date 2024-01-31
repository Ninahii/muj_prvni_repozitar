import sys
import random
import pygame
pygame.init()

rozliseni_okna = (800, 1000)
okno = pygame.display.set_mode(rozliseni_okna)

pozice_cara_x = 0
pozice_cara_y = 600
velikost_cara_x = 800
velikost_cara_y = 5

pozicee_hlavne_x = 363
pozicee_hlavne_y = 770
velikostt_hlavne_x = 15
velikostt_hlavne_y = 30
rychlost_hlavne_y = 1

terc_pocet_radku = 3
terc_pocet_sloupcu = 8
terc_velikost_x = 25
terc_velikost_y = 25
terc_posun_x = 100
terc_posun_y = 100



terce = []
for i in range(terc_pocet_radku):
    for j in range(terc_pocet_sloupcu):
        terce.append((50 + j * terc_posun_x, 50 + i * terc_posun_y))


polomer_kulicky = 10
rychlost_kulicky = 1
kulicky = []



while True:
    stisknute_klavesy = pygame.key.get_pressed()

    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if stisknute_klavesy[pygame.K_LEFT]:
        pozicee_hlavne_x -= rychlost_hlavne_y

    if stisknute_klavesy[pygame.K_RIGHT]:
        pozicee_hlavne_x += rychlost_hlavne_y

    if stisknute_klavesy[pygame.K_SPACE] and not any(kulicka for kulicka in kulicky if kulicka[1] > 0):
        pozice_kulicky_x, pozice_kulicky_y = pozicee_hlavne_x + velikostt_hlavne_x // 2, pozicee_hlavne_y
        kulicky.append((pozice_kulicky_x, pozice_kulicky_y))

    for i, (kulicka_x, kulicka_y) in enumerate(kulicky):
        kulicky[i] = (kulicka_x, kulicka_y - rychlost_kulicky)

    kulicky = [(kulicka_x, kulicka_y) for kulicka_x, kulicka_y in kulicky if kulicka_y > 0]

    if pozicee_hlavne_x + velikostt_hlavne_x >= rozliseni_okna[0]:
        pozicee_hlavne_x = rozliseni_okna[0] - velikostt_hlavne_x

    if pozicee_hlavne_x < 0:
        pozicee_hlavne_x = 0




    for kulicka_x, kulicka_y in kulicky:
        for terc_index, (terc_x, terc_y) in enumerate(terce):
            if (
                terc_x < kulicka_x < terc_x + terc_velikost_x and
                terc_y < kulicka_y < terc_y + terc_velikost_y
            ):
                kulicky.remove((kulicka_x, kulicka_y))
                del terce[terc_index]
                break

            
            
    if not terce:
        print()
        print("Všechny terče zničeny! Vyhrál si!")
        pygame.quit()
        sys.exit()


 #design---------
    okno.fill((0, 0, 0))

    for kulicka_x, kulicka_y in kulicky:
        pygame.draw.ellipse(okno, (255, 0, 255), (kulicka_x - polomer_kulicky, kulicka_y - polomer_kulicky, polomer_kulicky * 2, polomer_kulicky * 2))



    pygame.draw.rect(okno, (255, 255, 255), (pozice_cara_x, pozice_cara_y, velikost_cara_x, velikost_cara_y))
    pygame.draw.rect(okno, (0, 255, 0), (pozicee_hlavne_x, pozicee_hlavne_y, velikostt_hlavne_x, velikostt_hlavne_y))

    for terc_x, terc_y in terce:
        pygame.draw.rect(okno, (255, 0, 0), (terc_x, terc_y, terc_velikost_x, terc_velikost_y))

    pygame.display.update()





