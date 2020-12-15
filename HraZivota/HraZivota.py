#instalace modulu pygame: https://www.pygame.org/wiki/GettingStarted
import sys
import pygame #https://www.pygame.org/docs/tut/PygameIntro.html

OBRAZOVKA = SIRKA, VYSKA = 640, 480 #rozliseni
MRTVA_BUNKA = 0, 0, 0 #RGB 8bit cerna obrazovka
ZIVA_BUNKA = 255, 0, 255 #magenta

class Hra: #tvorba tridy

    def __init__(self): #metodu zavola python vzdycky, kdyz vytvori novy objekt
        pygame.init() #inicializuje vsechny pygame moduly
        self.screen = pygame.display.set_mode(OBRAZOVKA) #tvorba grafickeho okna, cokoliv do nej nakreslime se zobrazi na obrazovce

    def spust(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit() #modul pygame ma ruzny promenny pro ruzny typy (atribut)
                                                         #kontrolujeme, jestli ma objekt event atribut quit, pokud ano, zavolam sys.exit()
                                                         #ktery program vypne
                                                         #pygame.quit() - opak pygame.init() -> jakoby deaktivuje pygame

            self.screen.fill(MRTVA_BUNKA)

            #screen.blit(ball, ballrect) #=block transfer vykresli obraz do pameti, ktera ale jeste neni zobrazena
            pygame.display.flip() #aktualizuje obsah obrazovky - vsechno co jsme nakreslili na obrazovku se vizualizuje


hra = Hra() #tvorba objektu
hra.spust()

