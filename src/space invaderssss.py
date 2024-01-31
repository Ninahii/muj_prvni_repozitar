import sys
import random
import pygame
pygame.init()

rozliseni_okna = (800, 1000 )

okno = pygame.display.set_mode(rozliseni_okna)



#SOUŘADNICE

pozice_cara_x = 0
pozice_cara_y = 600
velikost_cara_x = 800
velikost_cara_y = 5

pozice_hlcasti_x = 350
pozice_hlcasti_y = 800
velikost_hlcasti_x = 40
velikost_hlcasti_y = 60
rychlost_hlcasti = 2

pozice_scasti_x = 390
pozice_scasti_y = 830
velikost_scasti_x = 20
velikost_scasti_y = 30
rychlost_scasti = 2

pozicee_scasti_x = 330
pozicee_scasti_y = 830
velikostt_scasti_x = 20
velikostt_scasti_y = 30
rychlostt_scasti = 2

pozicee_hlavne_x = 363
pozicee_hlavne_y = 770
velikostt_hlavne_x = 15
velikostt_hlavne_y = 30
rychlost_hlavne_y = 1






#střílecí terče_______________________________________
pozice_t1_x = 50
pozice_t1_y = 50
velikost_t1_x = 25
velikost_t1_y = 25

pozice_t2_x = 150
pozice_t2_y = 50
velikost_t2_x = 25
velikost_t2_y = 25

pozice_t3_x = 250
pozice_t3_y = 50
velikost_t3_x = 25
velikost_t3_y = 25

pozice_t4_x = 350
pozice_t4_y = 50
velikost_t4_x = 25
velikost_t4_y = 25

pozice_t5_x = 450
pozice_t5_y = 50
velikost_t5_x = 25
velikost_t5_y = 25

pozice_t6_x = 550
pozice_t6_y = 50
velikost_t6_x = 25
velikost_t6_y = 25

pozice_t7_x = 650
pozice_t7_y = 50
velikost_t7_x = 25
velikost_t7_y = 25

pozice_t8_x = 750
pozice_t8_y = 50
velikost_t8_x = 25
velikost_t8_y = 25

            #2 radek
pozice2_t1_x = 50
pozice2_t1_y = 150
velikost2_t1_x = 25
velikost2_t1_y = 25

pozice2_t2_x = 150
pozice2_t2_y = 150
velikost2_t2_x = 25
velikost2_t2_y = 25

pozice2_t3_x = 250
pozice2_t3_y = 150
velikost2_t3_x = 25
velikost2_t3_y = 25

pozice2_t4_x = 350
pozice2_t4_y = 150
velikost2_t4_x = 25
velikost2_t4_y = 25

pozice2_t5_x = 450
pozice2_t5_y = 150
velikost2_t5_x = 25
velikost2_t5_y = 25

pozice2_t6_x = 550
pozice2_t6_y = 150
velikost2_t6_x = 25
velikost2_t6_y = 25

pozice2_t7_x = 650
pozice2_t7_y = 150
velikost2_t7_x = 25
velikost2_t7_y = 25

pozice2_t8_x = 750
pozice2_t8_y = 150
velikost2_t8_x = 25
velikost2_t8_y = 25

        #radek 3

pozice3_t1_x = 50
pozice3_t1_y = 250
velikost3_t1_x = 25
velikost3_t1_y = 25

pozice3_t2_x = 150
pozice3_t2_y = 250
velikost3_t2_x = 25
velikost3_t2_y = 25

pozice3_t3_x = 250
pozice3_t3_y = 250
velikost3_t3_x = 25
velikost3_t3_y = 25

pozice3_t4_x = 350
pozice3_t4_y = 250
velikost3_t4_x = 25
velikost3_t4_y = 25

pozice3_t5_x = 450
pozice3_t5_y = 250
velikost3_t5_x = 25
velikost3_t5_y = 25

pozice3_t6_x = 550
pozice3_t6_y = 250
velikost3_t6_x = 25
velikost3_t6_y = 25

pozice3_t7_x = 650
pozice3_t7_y = 250
velikost3_t7_x = 25
velikost3_t7_y = 25

pozice3_t8_x = 750
pozice3_t8_y = 250
velikost3_t8_x = 25
velikost3_t8_y = 25

pozice_kulicky_x = 400
pozice_kulicky_y = 500
velikost_kulicky_x = 10
velikost_kulicky_y = 10
rychlost_kulicky_x = 1
rychlost_kulicky_y = 2







while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    stisknute_klavesy = pygame.key.get_pressed()
            
    if stisknute_klavesy[pygame.K_LEFT]:
        pozice_hlcasti_x -= rychlost_hlcasti
        pozice_scasti_x -= rychlost_scasti
        pozicee_scasti_x -= rychlostt_scasti
        pozicee_hlavne_x -= rychlost_hlavne_y
        
    if stisknute_klavesy[pygame.K_RIGHT]:
        pozice_hlcasti_x += rychlost_hlcasti
        pozice_scasti_x += rychlost_scasti
        pozicee_scasti_x += rychlostt_scasti
        pozicee_hlavne_x += rychlost_hlavne_y
        
        
    if stisknute_klavesy[pygame.K_SPACE]:
        pygame.draw.ellipse(okno, (255, 0, 255), (pozice_kulicky_x, pozice_kulicky_y, velikost_kulicky_x, velikost_kulicky_y))
        pozice_kulicky_y -= rychlost_kulicky_y 
        
        





    if pozicee_hlavne_x + velikostt_hlavne_x >= rozliseni_okna[0]:
        pozicee_hlavne_x + velikostt_hlavne_x
        pozicee_hlavne_x = rozliseni_okna[0] - velikostt_hlavne_x

    if pozicee_hlavne_x < 0:
        pozicee_hlavne_x = rozliseni_okna[0] - rozliseni_okna [0]


#design
        
    okno.fill((0, 0, 0 ))
   
            
    pygame.draw.rect(okno, (255, 255, 255), (pozice_cara_x, pozice_cara_y, velikost_cara_x, velikost_cara_y))
    #pygame.draw.rect(okno, (0, 255, 0), (pozice_hlcasti_x, pozice_hlcasti_y, velikost_hlcasti_x, velikost_hlcasti_y))
    #pygame.draw.rect(okno, (0, 255, 0), (pozice_scasti_x, pozice_scasti_y, velikost_scasti_x, velikost_scasti_y))
    #pygame.draw.rect(okno, (0, 255, 0), (pozicee_scasti_x, pozicee_scasti_y, velikostt_scasti_x, velikostt_scasti_y))
    pygame.draw.rect(okno, (0, 255, 0), (pozicee_hlavne_x, pozicee_hlavne_y, velikostt_hlavne_x, velikostt_hlavne_y))
    
    pygame.draw.ellipse(okno, (255, 0, 255), (pozice_kulicky_x, pozice_kulicky_y, velikost_kulicky_x, velikost_kulicky_y))
    
    
    #aliens (nepřátelé) radek 1
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t1_x, pozice_t1_y, velikost_t1_x, velikost_t1_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t2_x, pozice_t2_y, velikost_t2_x, velikost_t2_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t3_x, pozice_t3_y, velikost_t3_x, velikost_t3_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t4_x, pozice_t4_y, velikost_t4_x, velikost_t4_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t5_x, pozice_t5_y, velikost_t5_x, velikost_t5_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t6_x, pozice_t6_y, velikost_t6_x, velikost_t6_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t7_x, pozice_t7_y, velikost_t7_x, velikost_t7_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice_t8_x, pozice_t8_y, velikost_t8_x, velikost_t8_y))
            #radek 2
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t1_x, pozice2_t1_y, velikost2_t1_x, velikost2_t1_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t2_x, pozice2_t2_y, velikost2_t2_x, velikost2_t2_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t3_x, pozice2_t3_y, velikost2_t3_x, velikost2_t3_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t4_x, pozice2_t4_y, velikost2_t4_x, velikost2_t4_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t5_x, pozice2_t5_y, velikost2_t5_x, velikost2_t5_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t6_x, pozice2_t6_y, velikost2_t6_x, velikost2_t6_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t7_x, pozice2_t7_y, velikost2_t7_x, velikost2_t7_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice2_t8_x, pozice2_t8_y, velikost2_t8_x, velikost2_t8_y))
            #radek 3
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t1_x, pozice3_t1_y, velikost3_t1_x, velikost3_t1_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t2_x, pozice3_t2_y, velikost3_t2_x, velikost3_t2_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t3_x, pozice3_t3_y, velikost3_t3_x, velikost3_t3_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t4_x, pozice3_t4_y, velikost3_t4_x, velikost3_t4_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t5_x, pozice3_t5_y, velikost3_t5_x, velikost3_t5_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t6_x, pozice3_t6_y, velikost3_t6_x, velikost3_t6_x))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t7_x, pozice3_t7_y, velikost3_t7_x, velikost3_t7_y))
    pygame.draw.rect(okno, (255, 0, 0), (pozice3_t8_x, pozice3_t8_y, velikost3_t8_x, velikost3_t8_y))
    
        
    
    
    pygame.display.update()
