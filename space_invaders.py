import sys
import random
import pygame
pygame.init()

rozliseni_okna = (800,900 )

okno = pygame.display.set_mode(rozliseni_okna)
       
#SOUŘADNICE

pozice_micku_x = 300
pozice_micku_y = 300
velikost_micku = 50
rychlost_micku_x = 0.6
rychlost_micku_y = 0.6

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    stisknute_klavesy = pygame.key.get_pressed()
          
#OVLÁDÁNÍ CHYTAČŮ
        
    if stisknute_klavesy[pygame.K_s]:
        pozice_obdelniku1_y += rychlost_obdelniku1
        
    if stisknute_klavesy[pygame.K_w]:
        pozice_obdelniku1_y -= rychlost_obdelniku1
        
    if stisknute_klavesy[pygame.K_DOWN]:
        pozice_obdelniku2_y += rychlost_obdelniku2
        
    if stisknute_klavesy[pygame.K_UP]:
        pozice_obdelniku2_y -= rychlost_obdelniku2
#END CHYTAČŮ



    okno.fill((19, 19, 19))

    pygame.draw.ellipse(okno, (170, 57, 57), (pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku))
    
    pygame.display.update()    