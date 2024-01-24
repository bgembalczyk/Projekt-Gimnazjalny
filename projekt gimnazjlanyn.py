# gorna, przednia, prawa, tylna, lewa, dolna
# 5 - bialy, 4 - pomaranczowy, 1 - niebieski, 2 - czerwony, 3 - zielony, 0 - zolty
# 35 welna; 0 - white; 1 - orange; 4 - yellow; 5 - green; 11 - blue; 14 - red; 15 - black;
#URFDLByxz

from random import randint
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

kostka = [[["yellow", "yellow"], ["yellow", "yellow"]], [["blue", "blue"], ["blue", "blue"]], [["red", "red"], ["red", "red"]], [["green", "green"], ["green", "green"]], [["orange", "orange"], ["orange", "orange"]], [["white", "white"], ["white", "white"]]]
kostkaKoniec = [[["yellow", "yellow"], ["yellow", "yellow"]], [["blue", "blue"], ["blue", "blue"]], [["red", "red"], ["red", "red"]], [["green", "green"], ["green", "green"]], [["orange", "orange"], ["orange", "orange"]], [["white", "white"], ["white", "white"]]]
#kostkaTest = [[["yellow1", "yellow2"], ["yellow3", "yellow4"]], [["blue1", "blue2"], ["blue3", "blue4"]], [["red1", "red2"], ["red3", "red4"]], [["green1", "green2"], ["green3", "green4"]], [["orange", "orange"], ["orange", "orange"]], [["white1", "white2"], ["white3", "white4"]]] 

mc = Minecraft.create()
mc.postToChat("Hello world")
mc.player.setPos(-20, 40, 20)
n = 1

def czysc():
    mc.setBlocks(200, 0, 200, -200, 200, -200, 0)

def kolor(kol):
    if kol == "white":
        return 0
    if kol == "orange":
        return 1
    if kol == "yellow":
        return 4
    if kol == "green":
        return 5
    if kol == "blue":
        return 11
    if kol == "red":
        return 14

def rysuj(lista):

    czysc()

    #mc.setBlocks(-5, 31, -5, 5, 21, 5, 46)

    mc.setBlocks(0, 20, -6, 0, 20, 6, 35, 15)
    mc.setBlocks(-6, 20, 0, 6, 20, 0, 35, 15)

    mc.setBlocks(-6, 20, -6, 6, 20, -6, 35, 15)
    mc.setBlocks(6, 20, -6, 6, 20, 6, 35, 15)
    mc.setBlocks(6, 20, 6, -6, 20, 6, 35, 15)
    mc.setBlocks(-6, 20, 6, -6, 20, -6, 35, 15)

    mc.setBlocks(6, 20, -6, 6, 32, -6, 35, 15)
    mc.setBlocks(-6, 20, -6, -6, 32, -6, 35, 15)
    mc.setBlocks(-6, 20, 6, -6, 32, 6, 35, 15)
    mc.setBlocks(6, 20, 6, 6, 32, 6, 35, 15)

    mc.setBlocks(0, 20, -6, 0, 32, -6, 35, 15)
    mc.setBlocks(-6, 20, 0, -6, 32, 0, 35, 15)
    mc.setBlocks(0, 20, 6, 0, 32, 6, 35, 15)
    mc.setBlocks(6, 20, 0, 6, 32, 0, 35, 15)

    mc.setBlocks(-6, 26, -6, 6, 26, -6, 35, 15)
    mc.setBlocks(6, 26, -6, 6, 26, 6, 35, 15)
    mc.setBlocks(6, 26, 6, -6, 26, 6, 35, 15)
    mc.setBlocks(-6, 26, 6, -6, 26, -6, 35, 15)

    mc.setBlocks(-6, 32, -6, 6, 32, -6, 35, 15)
    mc.setBlocks(6, 32, -6, 6, 32, 6, 35, 15)
    mc.setBlocks(6, 32, 6, -6, 32, 6, 35, 15)
    mc.setBlocks(-6, 32, 6, -6, 32, -6, 35, 15)

    mc.setBlocks(0, 32, -6, 0, 32, 6, 35, 15)
    mc.setBlocks(-6, 32, 0, 6, 32, 0, 35, 15)

    mc.setBlocks(5, 32, -5, 1, 32, -1, 35, kolor(lista[0][0][0]))
    mc.setBlocks(5, 32, 1, 1, 32, 5, 35, kolor(lista[0][0][1]))
    mc.setBlocks(-1, 32, -5, -5, 32, -1, 35, kolor(lista[0][1][0]))
    mc.setBlocks(-1, 32, 1, -5, 32, 5, 35, kolor(lista[0][1][1]))

    mc.setBlocks(-6, 31, -5, -6, 27, -1, 35, kolor(lista[1][0][0]))
    mc.setBlocks(-6, 31, 1, -6, 27, 5, 35, kolor(lista[1][0][1]))
    mc.setBlocks(-6, 25, -5, -6, 21, -1, 35, kolor(lista[1][1][0]))
    mc.setBlocks(-6, 25, 1, -6, 21, 5, 35, kolor(lista[1][1][1]))

    mc.setBlocks(-5, 31, 6, -1, 27, 6, 35, kolor(lista[2][0][0]))
    mc.setBlocks(1, 31, 6, 5, 27, 6, 35, kolor(lista[2][0][1]))
    mc.setBlocks(-5, 25, 6, -1, 21, 6, 35, kolor(lista[2][1][0]))
    mc.setBlocks(1, 25, 6, 5, 21, 6, 35, kolor(lista[2][1][1]))

    mc.setBlocks(6, 31, 5, 6, 27, 1, 35, kolor(lista[3][0][0]))
    mc.setBlocks(6, 31, -1, 6, 27, -5, 35, kolor(lista[3][0][1]))
    mc.setBlocks(6, 25, 5, 6, 21, 1, 35, kolor(lista[3][1][0]))
    mc.setBlocks(6, 25, -1, 6, 21, -5, 35, kolor(lista[3][1][1]))

    mc.setBlocks(5, 31, -6, 1, 27, -6, 35, kolor(lista[4][0][0]))
    mc.setBlocks(-1, 31, -6, -5, 27, -6, 35, kolor(lista[4][0][1]))
    mc.setBlocks(5, 25, -6, 1, 21, -6, 35, kolor(lista[4][1][0]))
    mc.setBlocks(-1, 25, -6, -5, 21, -6, 35, kolor(lista[4][1][1]))

    mc.setBlocks(-5, 20, -5, -1, 20, -1, 35, kolor(lista[5][0][0]))
    mc.setBlocks(-5, 20, 1, -1, 20, 5, 35, kolor(lista[5][0][1]))
    mc.setBlocks(1, 20, -5, 5, 20, -1, 35, kolor(lista[5][1][0]))
    mc.setBlocks(1, 20, 1, 5, 20, 5, 35, kolor(lista[5][1][1]))

def pokaz(lista):
    pom = ["gorna", "przednia", "prawa", "tylna", "lewa", "dolna"]
    for i in range(len(lista)):
        print(pom[i])
        print(lista[i][0])
        print(lista[i][1])
    rysuj(lista)
    sleep(1)
    print

def ruch_U(lista, war):
    pom = lista[0][0][0]
    lista[0][0][0] = lista[0][1][0]
    lista[0][1][0] = lista[0][1][1]
    lista[0][1][1] = lista[0][0][1]
    lista[0][0][1] = pom
    
    pom = lista[4][0]
    lista[4][0] = lista[1][0]
    lista[1][0] = lista[2][0]
    lista[2][0] = lista[3][0]
    lista[3][0] = pom

    if war:
        mc.setBlocks(-6, 29, -5, -6, 29, -1, 35, 2)
        mc.setBlocks(-6, 29, 5, -6, 29, 1, 35, 2)
        mc.setBlocks(-5, 29, 6, -1, 29, 6, 35, 2)
        mc.setBlocks(5, 29, 6, 1, 29, 6, 35, 2)
        mc.setBlocks(6, 29, 5, 6, 29, 1, 35, 2)
        mc.setBlocks(6, 29, -5, 6, 29, -1, 35, 2)
        mc.setBlocks(5, 29, -6, 1, 29, -6, 35, 2)
        mc.setBlocks(-5, 29, -6, -1, 29, -6, 35, 2)

        mc.setBlocks(-3, 32, 5, -3, 32, 1, 35, 2)
        mc.setBlocks(-1, 32, -3, -5, 32, -3, 35, 2)
        mc.setBlocks(3, 32, -5, 3, 32, -1, 35, 2)
        mc.setBlocks(1, 32, 3, 5, 32, 3, 35, 2)

        mc.setBlocks(-6, 28, -4, -6, 30, -4, 35, 2)
        mc.setBlocks(-6, 28, 2, -6, 30, 2, 35, 2)
        mc.setBlocks(-4, 28, 6, -4, 30, 6, 35, 2)
        mc.setBlocks(2, 28, 6, 2, 30, 6, 35, 2)
        mc.setBlocks(6, 28, 4, 6, 30, 4, 35, 2)
        mc.setBlocks(6, 28, -2, 6, 30, -2, 35, 2)
        mc.setBlocks(4, 28, -6, 4, 30, -6, 35, 2)
        mc.setBlocks(-2, 28, -6, -2, 30, -6, 35, 2)

        mc.setBlocks(-2, 32, -4, -2, 32, -2, 35, 2)
        mc.setBlocks(4, 32, -2, 2, 32, -2, 35, 2)
        mc.setBlocks(2, 32, 4, 2, 32, 2, 35, 2)
        mc.setBlocks(-4, 32, 2, -2, 32, 2, 35, 2)

        sleep(1)
    
    return lista

def ruch_R(lista, war):
    pom = lista[2][0][0]
    lista[2][0][0] = lista[2][1][0]
    lista[2][1][0] = lista[2][1][1]
    lista[2][1][1] = lista[2][0][1]
    lista[2][0][1] = pom

    pom1 = lista[1][0][1]
    pom2 = lista[1][1][1]
    lista[1][0][1] = lista[5][0][1]
    lista[1][1][1] = lista[5][1][1]
    lista[5][0][1] = lista[3][1][0]
    lista[5][1][1] = lista[3][0][0]
    lista[3][1][0] = lista[0][0][1]
    lista[3][0][0] = lista[0][1][1]
    lista[0][0][1] = pom1
    lista[0][1][1] = pom2

    if war:
        mc.setBlocks(-6, 21, 3, -6, 25, 3, 35, 2)
        mc.setBlocks(-6, 27, 3, -6, 31, 3, 35, 2)        
        mc.setBlocks(-5, 32, 3, -1, 32, 3, 35, 2)        
        mc.setBlocks(5, 32, 3, 1, 32, 3, 35, 2)        
        mc.setBlocks(6, 21, 3, 6, 25, 3, 35, 2)
        mc.setBlocks(6, 27, 3, 6, 31, 3, 35, 2)        
        mc.setBlocks(-5, 20, 3, -1, 20, 3, 35, 2)        
        mc.setBlocks(5, 20, 3, 1, 20, 3, 35, 2)        

        mc.setBlocks(-5, 29, 6, -1, 29, 6, 35, 2)        
        mc.setBlocks(3, 31, 6, 3, 27, 6, 35, 2)        
        mc.setBlocks(5, 23, 6, 1, 23, 6, 35, 2)        
        mc.setBlocks(-3, 25, 6, -3, 21, 6, 35, 2)        

        mc.setBlocks(-6, 24, 2, -6, 24, 4, 35, 2)        
        mc.setBlocks(-6, 30, 2, -6, 30, 4, 35, 2)        
        mc.setBlocks(-2, 32, 2, -2, 32, 4, 35, 2)        
        mc.setBlocks(4, 32, 2, 4, 32, 4, 35, 2)        
        mc.setBlocks(6, 28, 2, 6, 28, 4, 35, 2)        
        mc.setBlocks(6, 22, 2, 6, 22, 4, 35, 2)        
        mc.setBlocks(2, 20, 4, 2, 20, 2, 35, 2)        
        mc.setBlocks(-4, 20, 4, -4, 20, 2, 35, 2)        

        mc.setBlocks(-2, 28, 6, -2, 30, 6, 35, 2)        
        mc.setBlocks(2, 28, 6, 4, 28, 6, 35, 2)        
        mc.setBlocks(2, 22, 6, 2, 24, 6, 35, 2)        
        mc.setBlocks(-4, 24, 6, -2, 24, 6, 35, 2)        
        
        sleep(1)
    
    return lista

def ruch_F(lista, war):
    pom = lista[1][0][0]
    lista[1][0][0] = lista[1][1][0]
    lista[1][1][0] = lista[1][1][1]
    lista[1][1][1] = lista[1][0][1]
    lista[1][0][1] = pom

    pom1 = lista[0][1][0]
    pom2 = lista[0][1][1]
    lista[0][1][0] = lista[4][1][1]
    lista[0][1][1] = lista[4][0][1]
    lista[4][1][1] = lista[5][0][1]
    lista[4][0][1] = lista[5][0][0]
    lista[5][0][1] = lista[2][0][0]
    lista[5][0][0] = lista[2][1][0]
    lista[2][0][0] = pom1
    lista[2][1][0] = pom2

    if war:
        mc.setBlocks(-3, 32, -5, -3, 32, -1, 35, 2)
        mc.setBlocks(-3, 32, 5, -3, 32, 1, 35, 2)
        mc.setBlocks(-3, 31, 6, -3, 27, 6, 35, 2)
        mc.setBlocks(-3, 25, 6, -3, 21, 6, 35, 2)
        mc.setBlocks(-3, 20, -5, -3, 20, -1, 35, 2)
        mc.setBlocks(-3, 20, 5, -3, 20, 1, 35, 2)
        mc.setBlocks(-3, 31, -6, -3, 27, -6, 35, 2)
        mc.setBlocks(-3, 25, -6, -3, 21, -6, 35, 2)

        mc.setBlocks(-6, 29, -5, -6, 29, -1, 35, 2)
        mc.setBlocks(-6, 31, 3, -6, 27, 3, 35, 2)
        mc.setBlocks(-6, 23, 5, -6, 23, 1, 35, 2)
        mc.setBlocks(-6, 25, -3, -6, 21, -3, 35, 2)

        mc.setBlocks(-2, 32, -2, -4, 32, -2, 35, 2)
        mc.setBlocks(-2, 32, 4, -4, 32, 4, 35, 2)
        mc.setBlocks(-4, 28, 6, -2, 28, 6, 35, 2)
        mc.setBlocks(-4, 22, 6, -2, 22, 6, 35, 2)
        mc.setBlocks(-2, 20, 2, -4, 20, 2, 35, 2)
        mc.setBlocks(-2, 20, -4, -4, 20, -4, 35, 2)
        mc.setBlocks(-4, 30, -6, -2, 30, -6, 35, 2)
        mc.setBlocks(-4, 24, -6, -2, 24, -6, 35, 2)

        mc.setBlocks(-6, 28, -2, -6, 30, -2, 35, 2)
        mc.setBlocks(-6, 28, 2, -6, 28, 4, 35, 2)
        mc.setBlocks(-6, 22, 2, -6, 24, 2, 35, 2)
        mc.setBlocks(-6, 24, -4, -6, 24, -2, 35, 2)

        sleep(1)
    
    return lista

def ruch_Y(lista, war):
    pom = lista[1]
    lista[1] = lista[2]
    lista[2] = lista[3]
    lista[3] = lista[4]
    lista[4] = pom

    pom = lista[0][0][0]
    lista[0][0][0] = lista[0][1][0]
    lista[0][1][0] = lista[0][1][1]
    lista[0][1][1] = lista[0][0][1]
    lista[0][0][1] = pom

    pom = lista[5][0][0]
    lista[5][0][0] = lista[5][0][1]
    lista[5][0][1] = lista[5][1][1]
    lista[5][1][1] = lista[5][1][0]
    lista[5][1][0] = pom

    if war:
        mc.setBlocks(-6, 29, -5, -6, 29, -1, 35, 2)
        mc.setBlocks(-6, 29, 5, -6, 29, 1, 35, 2)
        mc.setBlocks(-5, 29, 6, -1, 29, 6, 35, 2)
        mc.setBlocks(5, 29, 6, 1, 29, 6, 35, 2)
        mc.setBlocks(6, 29, 5, 6, 29, 1, 35, 2)
        mc.setBlocks(6, 29, -5, 6, 29, -1, 35, 2)
        mc.setBlocks(5, 29, -6, 1, 29, -6, 35, 2)
        mc.setBlocks(-5, 29, -6, -1, 29, -6, 35, 2)

        mc.setBlocks(-6, 23, -5, -6, 23, -1, 35, 2)
        mc.setBlocks(-6, 23, 5, -6, 23, 1, 35, 2)
        mc.setBlocks(-5, 23, 6, -1, 23, 6, 35, 2)
        mc.setBlocks(5, 23, 6, 1, 23, 6, 35, 2)
        mc.setBlocks(6, 23, 5, 6, 23, 1, 35, 2)
        mc.setBlocks(6, 23, -5, 6, 23, -1, 35, 2)
        mc.setBlocks(5, 23, -6, 1, 23, -6, 35, 2)
        mc.setBlocks(-5, 23, -6, -1, 23, -6, 35, 2)

        mc.setBlocks(-3, 32, 5, -3, 32, 1, 35, 2)
        mc.setBlocks(-1, 32, -3, -5, 32, -3, 35, 2)
        mc.setBlocks(3, 32, -5, 3, 32, -1, 35, 2)
        mc.setBlocks(1, 32, 3, 5, 32, 3, 35, 2)

        mc.setBlocks(-3, 20, 5, -3, 20, 1, 35, 2)
        mc.setBlocks(-1, 20, -3, -5, 20, -3, 35, 2)
        mc.setBlocks(3, 20, -5, 3, 20, -1, 35, 2)
        mc.setBlocks(1, 20, 3, 5, 20, 3, 35, 2)

        mc.setBlocks(-6, 28, -4, -6, 30, -4, 35, 2)
        mc.setBlocks(-6, 28, 2, -6, 30, 2, 35, 2)
        mc.setBlocks(-4, 28, 6, -4, 30, 6, 35, 2)
        mc.setBlocks(2, 28, 6, 2, 30, 6, 35, 2)
        mc.setBlocks(6, 28, 4, 6, 30, 4, 35, 2)
        mc.setBlocks(6, 28, -2, 6, 30, -2, 35, 2)
        mc.setBlocks(4, 28, -6, 4, 30, -6, 35, 2)
        mc.setBlocks(-2, 28, -6, -2, 30, -6, 35, 2)

        mc.setBlocks(-6, 22, -4, -6, 24, -4, 35, 2)
        mc.setBlocks(-6, 22, 2, -6, 24, 2, 35, 2)
        mc.setBlocks(-4, 22, 6, -4, 24, 6, 35, 2)
        mc.setBlocks(2, 22, 6, 2, 24, 6, 35, 2)
        mc.setBlocks(6, 22, 4, 6, 24, 4, 35, 2)
        mc.setBlocks(6, 22, -2, 6, 24, -2, 35, 2)
        mc.setBlocks(4, 22, -6, 4, 24, -6, 35, 2)
        mc.setBlocks(-2, 22, -6, -2, 24, -6, 35, 2)

        mc.setBlocks(-2, 32, -4, -2, 32, -2, 35, 2)
        mc.setBlocks(4, 32, -2, 2, 32, -2, 35, 2)
        mc.setBlocks(2, 32, 4, 2, 32, 2, 35, 2)
        mc.setBlocks(-4, 32, 2, -2, 32, 2, 35, 2)

        mc.setBlocks(-2, 20, -4, -2, 20, -2, 35, 2)
        mc.setBlocks(4, 20, -2, 2, 20, -2, 35, 2)
        mc.setBlocks(2, 20, 4, 2, 20, 2, 35, 2)
        mc.setBlocks(-4, 20, 2, -2, 20, 2, 35, 2)

        sleep(1)

    return lista

def ruch_X(lista, war):
    pom1 = lista[0][0][0]
    pom2 = lista[0][0][1]
    pom3 = lista[0][1][0]
    pom4 = lista[0][1][1]
    lista[0][0][0] = lista[1][0][0]
    lista[0][0][1] = lista[1][0][1]
    lista[0][1][0] = lista[1][1][0]
    lista[0][1][1] = lista[1][1][1]
    lista[1][0][0] = lista[5][0][0]
    lista[1][0][1] = lista[5][0][1]
    lista[1][1][0] = lista[5][1][0]
    lista[1][1][1] = lista[5][1][1]
    lista[5][0][0] = lista[3][1][1]
    lista[5][0][1] = lista[3][1][0]
    lista[5][1][0] = lista[3][0][1]
    lista[5][1][1] = lista[3][0][0]
    lista[3][1][1] = pom1
    lista[3][1][0] = pom2
    lista[3][0][1] = pom3
    lista[3][0][0] = pom4

    pom = lista[2][0][0]
    lista[2][0][0] = lista[2][1][0]
    lista[2][1][0] = lista[2][1][1]
    lista[2][1][1] = lista[2][0][1]
    lista[2][0][1] = pom

    pom = lista[4][0][0]
    lista[4][0][0] = lista[4][0][1]
    lista[4][0][1] = lista[4][1][1]
    lista[4][1][1] = lista[4][1][0]
    lista[4][1][0] = pom
    
    if war:
        mc.setBlocks(-6, 21, 3, -6, 25, 3, 35, 2)
        mc.setBlocks(-6, 27, 3, -6, 31, 3, 35, 2)        
        mc.setBlocks(-5, 32, 3, -1, 32, 3, 35, 2)        
        mc.setBlocks(5, 32, 3, 1, 32, 3, 35, 2)        
        mc.setBlocks(6, 21, 3, 6, 25, 3, 35, 2)
        mc.setBlocks(6, 27, 3, 6, 31, 3, 35, 2)        
        mc.setBlocks(-5, 20, 3, -1, 20, 3, 35, 2)        
        mc.setBlocks(5, 20, 3, 1, 20, 3, 35, 2)        

        mc.setBlocks(-6, 21, -3, -6, 25, -3, 35, 2)
        mc.setBlocks(-6, 27, -3, -6, 31, -3, 35, 2)        
        mc.setBlocks(-5, 32, -3, -1, 32, -3, 35, 2)        
        mc.setBlocks(5, 32, -3, 1, 32, -3, 35, 2)        
        mc.setBlocks(6, 21, -3, 6, 25, -3, 35, 2)
        mc.setBlocks(6, 27, -3, 6, 31, -3, 35, 2)        
        mc.setBlocks(-5, 20, -3, -1, 20, -3, 35, 2)        
        mc.setBlocks(5, 20, -3, 1, 20, -3, 35, 2)        

        mc.setBlocks(-5, 29, 6, -1, 29, 6, 35, 2)        
        mc.setBlocks(3, 31, 6, 3, 27, 6, 35, 2)        
        mc.setBlocks(5, 23, 6, 1, 23, 6, 35, 2)        
        mc.setBlocks(-3, 25, 6, -3, 21, 6, 35, 2)        

        mc.setBlocks(-5, 29, -6, -1, 29, -6, 35, 2)        
        mc.setBlocks(3, 31, -6, 3, 27, -6, 35, 2)        
        mc.setBlocks(5, 23, -6, 1, 23, -6, 35, 2)        
        mc.setBlocks(-3, 25, -6, -3, 21, -6, 35, 2)        

        mc.setBlocks(-6, 24, 2, -6, 24, 4, 35, 2)        
        mc.setBlocks(-6, 30, 2, -6, 30, 4, 35, 2)        
        mc.setBlocks(-2, 32, 2, -2, 32, 4, 35, 2)        
        mc.setBlocks(4, 32, 2, 4, 32, 4, 35, 2)        
        mc.setBlocks(6, 28, 2, 6, 28, 4, 35, 2)        
        mc.setBlocks(6, 22, 2, 6, 22, 4, 35, 2)        
        mc.setBlocks(2, 20, 4, 2, 20, 2, 35, 2)        
        mc.setBlocks(-4, 20, 4, -4, 20, 2, 35, 2)        

        mc.setBlocks(-6, 24, -2, -6, 24, -4, 35, 2)        
        mc.setBlocks(-6, 30, -2, -6, 30, -4, 35, 2)        
        mc.setBlocks(-2, 32, -2, -2, 32, -4, 35, 2)        
        mc.setBlocks(4, 32, -2, 4, 32, -4, 35, 2)        
        mc.setBlocks(6, 28, -2, 6, 28, -4, 35, 2)        
        mc.setBlocks(6, 22, -2, 6, 22, -4, 35, 2)        
        mc.setBlocks(2, 20, -4, 2, 20, -2, 35, 2)        
        mc.setBlocks(-4, 20, -4, -4, 20, -2, 35, 2)        

        mc.setBlocks(-2, 28, 6, -2, 30, 6, 35, 2)        
        mc.setBlocks(2, 28, 6, 4, 28, 6, 35, 2)        
        mc.setBlocks(2, 22, 6, 2, 24, 6, 35, 2)        
        mc.setBlocks(-4, 24, 6, -2, 24, 6, 35, 2)        

        mc.setBlocks(-2, 28, -6, -2, 30, -6, 35, 2)        
        mc.setBlocks(2, 28, -6, 4, 28, -6, 35, 2)        
        mc.setBlocks(2, 22, -6, 2, 24, -6, 35, 2)        
        mc.setBlocks(-4, 24, -6, -2, 24, -6, 35, 2)        

        sleep(1)

    return lista

def ruch_Z(lista, war):
    pom1 = lista[0][0][0]
    pom2 = lista[0][0][1]
    pom3 = lista[0][1][0]
    pom4 = lista[0][1][1]
    lista[0][0][0] = lista[4][1][0]
    lista[0][0][1] = lista[4][0][0]
    lista[0][1][0] = lista[4][1][1]
    lista[0][1][1] = lista[4][0][1]
    lista[4][1][0] = lista[5][1][1]
    lista[4][0][0] = lista[5][1][0]
    lista[4][1][1] = lista[5][0][1]
    lista[4][0][1] = lista[5][0][0]
    lista[5][1][1] = lista[2][0][1]
    lista[5][1][0] = lista[2][1][1]
    lista[5][0][1] = lista[2][0][0]
    lista[5][0][0] = lista[2][1][0]
    lista[2][0][1] = pom1
    lista[2][1][1] = pom2
    lista[2][0][0] = pom3
    lista[2][1][0] = pom4

    pom = lista[1][0][0]
    lista[1][0][0] = lista[1][1][0]
    lista[1][1][0] = lista[1][1][1]
    lista[1][1][1] = lista[1][0][1]
    lista[1][0][1] = pom

    pom = lista[3][0][0]
    lista[3][0][0] = lista[3][0][1]
    lista[3][0][1] = lista[3][1][1]
    lista[3][1][1] = lista[3][1][0]
    lista[3][1][0] = pom

    if war:
        mc.setBlocks(-3, 32, -5, -3, 32, -1, 35, 2)
        mc.setBlocks(-3, 32, 5, -3, 32, 1, 35, 2)
        mc.setBlocks(-3, 31, 6, -3, 27, 6, 35, 2)
        mc.setBlocks(-3, 25, 6, -3, 21, 6, 35, 2)
        mc.setBlocks(-3, 20, -5, -3, 20, -1, 35, 2)
        mc.setBlocks(-3, 20, 5, -3, 20, 1, 35, 2)
        mc.setBlocks(-3, 31, -6, -3, 27, -6, 35, 2)
        mc.setBlocks(-3, 25, -6, -3, 21, -6, 35, 2)

        mc.setBlocks(3, 32, -5, 3, 32, -1, 35, 2)
        mc.setBlocks(3, 32, 5, 3, 32, 1, 35, 2)
        mc.setBlocks(3, 31, 6, 3, 27, 6, 35, 2)
        mc.setBlocks(3, 25, 6, 3, 21, 6, 35, 2)
        mc.setBlocks(3, 20, -5, 3, 20, -1, 35, 2)
        mc.setBlocks(3, 20, 5, 3, 20, 1, 35, 2)
        mc.setBlocks(3, 31, -6, 3, 27, -6, 35, 2)
        mc.setBlocks(3, 25, -6, 3, 21, -6, 35, 2)

        mc.setBlocks(-6, 29, -5, -6, 29, -1, 35, 2)
        mc.setBlocks(-6, 31, 3, -6, 27, 3, 35, 2)
        mc.setBlocks(-6, 23, 5, -6, 23, 1, 35, 2)
        mc.setBlocks(-6, 25, -3, -6, 21, -3, 35, 2)

        mc.setBlocks(6, 29, -5, 6, 29, -1, 35, 2)
        mc.setBlocks(6, 31, 3, 6, 27, 3, 35, 2)
        mc.setBlocks(6, 23, 5, 6, 23, 1, 35, 2)
        mc.setBlocks(6, 25, -3, 6, 21, -3, 35, 2)

        mc.setBlocks(-2, 32, -2, -4, 32, -2, 35, 2)
        mc.setBlocks(-2, 32, 4, -4, 32, 4, 35, 2)
        mc.setBlocks(-4, 28, 6, -2, 28, 6, 35, 2)
        mc.setBlocks(-4, 22, 6, -2, 22, 6, 35, 2)
        mc.setBlocks(-2, 20, 2, -4, 20, 2, 35, 2)
        mc.setBlocks(-2, 20, -4, -4, 20, -4, 35, 2)
        mc.setBlocks(-4, 30, -6, -2, 30, -6, 35, 2)
        mc.setBlocks(-4, 24, -6, -2, 24, -6, 35, 2)

        mc.setBlocks(2, 32, -2, 4, 32, -2, 35, 2)
        mc.setBlocks(2, 32, 4, 4, 32, 4, 35, 2)
        mc.setBlocks(4, 28, 6, 2, 28, 6, 35, 2)
        mc.setBlocks(4, 22, 6, 2, 22, 6, 35, 2)
        mc.setBlocks(2, 20, 2, 4, 20, 2, 35, 2)
        mc.setBlocks(2, 20, -4, 4, 20, -4, 35, 2)
        mc.setBlocks(4, 30, -6, 2, 30, -6, 35, 2)
        mc.setBlocks(4, 24, -6, 2, 24, -6, 35, 2)

        mc.setBlocks(-6, 28, -2, -6, 30, -2, 35, 2)
        mc.setBlocks(-6, 28, 2, -6, 28, 4, 35, 2)
        mc.setBlocks(-6, 22, 2, -6, 24, 2, 35, 2)
        mc.setBlocks(-6, 24, -4, -6, 24, -2, 35, 2)

        mc.setBlocks(6, 28, -2, 6, 30, -2, 35, 2)
        mc.setBlocks(6, 28, 2, 6, 28, 4, 35, 2)
        mc.setBlocks(6, 22, 2, 6, 24, 2, 35, 2)
        mc.setBlocks(6, 24, -4, 6, 24, -2, 35, 2)

        sleep(1)
        
    return lista

def algorytm(lista, rura):
    global n
    for i in rura:
        print(str(n) + " " + str(i))
        mc.postToChat(str(n) + " " + str(i))
        n = n + 1
        if i == "U":
            lista = ruch_U(lista, True)
        elif i == "R":
            lista = ruch_R(lista, True)
        elif i == "F":
            lista = ruch_F(lista, True)
        elif i == "D":
            lista = algorytm(lista, "UYYY")
        elif i == "L":
            lista = algorytm(lista, "RXXX")
        elif i == "B":
            lista = algorytm(lista, "FZZZ")
        elif i == "X":
            lista = ruch_X(lista, True)
        elif i == "Y":
            lista = ruch_Y(lista, True)
        elif i == "Z":
            lista = ruch_Z(lista, True)
        pokaz(lista)
    return lista

def pomieszaj(lista):
    for i in range(20):
        pom = randint(0, 2)
        if pom == 0:
            lista = ruch_U(lista, False)
        elif pom == 1:
            lista = ruch_R(lista, False)
        elif pom == 2:
            lista = ruch_F(lista, False)
    return lista

def czyUlozona(lista):
    pom = []
    for i in lista:
        if i[0][0] == i[0][1] and i[0][1] == i[1][0] and i[1][0] == i[1][1]:
            pom.append(True)
        else:
            pom.append(False)
    if False in pom:
        return False
    else:
        return True

def czyDwieParyTakieSame(lista, rura):
    for i in rura:
        if lista[1][1][0] == lista[1][1][1] and lista[5][0][0] == lista[5][0][1]:
            return lista
        lista = algorytm(lista, i)
    return False

def dolna(lista):
    pom = lista[5][0][0]
    ruchy = ""
    while len(ruchy) != 30:
        ruchy = ruchy + "UR"
    if czyDwieParyTakieSame(lista, ruchy) != False:
        lista = czyDwieParyTakieSame(lista, ruchy)
    else:
        lista = algorytm(lista, "B")
        lista = czyDwieParyTakieSame(lista, ruchy)
    lista = algorytm(lista, "Y")
    if czyDwieParyTakieSame(lista, ruchy) != False:
        lista = czyDwieParyTakieSame(lista, ruchy)
    else:
        lista = algorytm(lista, "UU")
        lista = czyDwieParyTakieSame(lista, ruchy)
    lista = algorytm(lista, "Y")
    if lista[5][0][1] == pom:
        return lista
    if lista[1][1][1] == pom or lista[2][1][0] == pom:
        lista = algorytm(lista, "RURRR")
    if lista[0][0][0] == pom or lista[0][0][1] == pom or lista[0][1][0] == pom or lista[0][1][1] == pom:
        while lista[0][1][1] != pom:
            lista = algorytm(lista, "U")
        lista = algorytm(lista, "RUUURRR")
    if lista[1][0][0] == pom or lista[2][0][0] == pom or lista[3][0][0] == pom or lista[4][0][0] == pom:
        while lista[2][0][0] != pom:
            lista = algorytm(lista, "U")
        lista = algorytm(lista, "FRRRFFFR")
    elif lista[1][0][1] == pom or lista[2][0][1] == pom or lista[3][0][1] == pom or lista[4][0][1] == pom:    
        while lista[1][0][1] != pom:
            lista = algorytm(lista, "U")
        lista = algorytm(lista, "RRRFRFFF")
    else:
        print("a tego nigdy nie powinno byc")
        pokaz(lista)
    return lista

def orientacjaOstatniejWarstwy(lista):
    ruchy = ["FRURRRUUUFFF", "RRRUUURULUUURRRUX", "XXXDRURRRDDDRUUURRRX", "LLLUUULUUULLLUUL", "RURRRURUURRR", "RRRUUURUUURRRURUUURRRUUR", "RUURRUUURRUUURRUUR"]
    if lista[5][0][0] == "white":
        pom = "yellow"
    elif lista[5][0][0] == "yellow":
        pom = "white"
    elif lista[5][0][0] == "green":
        pom = "blue"
    elif lista[5][0][0] == "blue":
        pom = "green"
    elif lista[5][0][0] == "red":
        pom = "orange"
    elif lista[5][0][0] == "orange":
        pom = "red"
    if lista[0][0][0] == pom and lista[0][0][1] == pom and lista[0][1][0] == pom and lista[0][1][1] == pom:
        print(-1)
        return lista

    elif lista[0][0][1] == pom and lista[0][1][1] == pom and lista[4][0][0] == pom and lista[4][0][1] == pom:
        print(0.1)
        lista = algorytm(lista, ruchy[0])
    elif lista[0][0][0] == pom and lista[0][0][1] == pom and lista[1][0][0] == pom and lista[1][0][1] == pom:
        print(0.2)
        lista = algorytm(lista, "Y" + ruchy[0])
    elif lista[0][0][0] == pom and lista[0][1][0] == pom and lista[2][0][0] == pom and lista[2][0][1] == pom:
        print(0.3)
        lista = algorytm(lista, "YY" + ruchy[0])
    elif lista[0][1][0] == pom and lista[0][1][1] == pom and lista[3][0][0] == pom and lista[3][0][1] == pom:
        print(0.4)
        lista = algorytm(lista, "YYY" + ruchy[0])
                
    elif lista[0][0][1] == pom and lista[0][1][1] == pom and lista[1][0][0] == pom and lista[3][0][1] == pom:
        print(1.1)
        lista = algorytm(lista, ruchy[1])
    elif lista[0][0][0] == pom and lista[0][0][1] == pom and lista[2][0][0] == pom and lista[4][0][1] == pom:
        print(1.2)
        lista = algorytm(lista, "Y" + ruchy[1])
    elif lista[0][0][0] == pom and lista[0][1][0] == pom and lista[3][0][0] == pom and lista[1][0][1] == pom:
        print(1.3)
        lista = algorytm(lista, "YY" + ruchy[1])
    elif lista[0][1][0] == pom and lista[0][1][1] == pom and lista[4][0][0] == pom and lista[2][0][1] == pom:
        print(1.4)
        lista = algorytm(lista, "YYY" + ruchy[1])
                
    elif lista[0][0][0] == pom and lista[0][1][1] == pom and lista[3][0][0] == pom and lista[4][0][1] == pom:
        print(2.1)
        lista = algorytm(lista, ruchy[2])
    elif lista[0][0][1] == pom and lista[0][1][0] == pom and lista[2][0][0] == pom and lista[3][0][1] == pom:
        print(2.2)
        lista = algorytm(lista, "YYY" + ruchy[2])
    elif lista[0][0][0] == pom and lista[0][1][1] == pom and lista[1][0][0] == pom and lista[2][0][1] == pom:
        print(2.3)
        lista = algorytm(lista, "YY" + ruchy[2])
    elif lista[0][0][1] == pom and lista[0][1][0] == pom and lista[4][0][0] == pom and lista[1][0][1] == pom:
        print(2.4)
        lista = algorytm(lista, "Y" + ruchy[2])
                
    elif lista[0][1][1] == pom and lista[1][0][0] == pom and lista[4][0][0] == pom and lista[3][0][0] == pom:
        print(3.1)
        lista = algorytm(lista, ruchy[3])
    elif lista[0][1][0] == pom and lista[4][0][0] == pom and lista[3][0][0] == pom and lista[2][0][0] == pom:
        print(3.2)
        lista = algorytm(lista, "YYY" + ruchy[3])
    elif lista[0][0][0] == pom and lista[3][0][0] == pom and lista[2][0][0] == pom and lista[1][0][0] == pom:
        print(3.3)
        lista = algorytm(lista, "YY" + ruchy[3])
    elif lista[0][0][1] == pom and lista[2][0][0] == pom and lista[1][0][0] == pom and lista[4][0][0] == pom:
        print(3.4)
        lista = algorytm(lista, "Y" + ruchy[3])
                
    elif lista[0][1][0] == pom and lista[3][0][1] == pom and lista[2][0][1] == pom and lista[1][0][1] == pom:
        print(4.1)
        lista = algorytm(lista, ruchy[4])
    elif lista[0][0][0] == pom and lista[2][0][1] == pom and lista[1][0][1] == pom and lista[4][0][1] == pom:
        print(4.2)
        lista = algorytm(lista, "YYY" + ruchy[4])
    elif lista[0][0][1] == pom and lista[1][0][1] == pom and lista[4][0][1] == pom and lista[3][0][1] == pom:
        print(4.3)
        lista = algorytm(lista, "YY" + ruchy[4])
    elif lista[0][1][1] == pom and lista[4][0][1] == pom and lista[3][0][1] == pom and lista[2][0][1] == pom:
        print(4.4)
        lista = algorytm(lista, "Y" + ruchy[4])
        
    elif lista[2][0][0] == pom and lista[2][0][1] == pom and lista[4][0][1] == pom and lista[4][0][0] == pom:
        print(5.1)
        lista = algorytm(lista, ruchy[5])
    elif lista[1][0][0] == pom and lista[1][0][1] == pom and lista[3][0][0] == pom and lista[3][0][1] == pom:
        print(5.2)
        lista = algorytm(lista, "Y" + ruchy[5])
                
    elif lista[4][0][0] == pom and lista[4][0][1] == pom and lista[3][0][0] == pom and lista[1][0][1] == pom:
        print(6.1)
        lista = algorytm(lista, ruchy[6])
    elif lista[3][0][0] == pom and lista[3][0][1] == pom and lista[2][0][0] == pom and lista[4][0][1] == pom:
        print(6.2)
        lista = algorytm(lista, "YYY" + ruchy[6])
    elif lista[2][0][0] == pom and lista[2][0][1] == pom and lista[1][0][0] == pom and lista[3][0][1] == pom:
        print(6.3)
        lista = algorytm(lista, "YY" + ruchy[6])
    elif lista[1][0][0] == pom and lista[1][0][1] == pom and lista[4][0][0] == pom and lista[2][0][1] == pom:
        print(6.4)
        lista = algorytm(lista, "Y" + ruchy[6])
    else:
        print("a tego nigdy nie powinno byc")
        pokaz(lista)

    return lista

def ustawWarstwe(lista):
    for i in range(4):
        for j in range(4):
            if lista[1][0][0] == lista[1][1][0] and lista[1][0][1] == lista[1][1][1]:
                lista = algorytm(lista, "YY")
                return lista
            lista = algorytm(lista, "U")
        lista = algorytm(lista, "Y")

    for i in range(4):
        for j in range(4):
            if lista[1][0][1] == lista[1][1][1] and lista[2][0][0] == lista[2][1][0]:
                return lista
            lista = algorytm(lista, "U")
        lista = algorytm(lista, "Y")

def permutacjaOstatniejWarstwy(lista):
    if lista[3][0][0] == lista[3][1][0] and lista[3][0][1] == lista[3][1][1]:
        lista = algorytm(lista, "RRRFRRRFFRUUURRRFFRR")
        lista = ustawWarstwe(lista)
        return lista
    else:
        lista = algorytm(lista, "FFUUURUUURRRUFFURURRR")
        lista = ustawWarstwe(lista)
        return lista        
                
def ukladaj():
    sleep(10)
    lista = pomieszaj(kostkaKoniec)
    print(czyUlozona(lista))
    print("kostka pomieszana")
    mc.postToChat("kostka pomieszana")
    pokaz(lista)
    if czyUlozona(lista):
        return "Udalo sie"
    sleep(5)
    lista = dolna(lista)
    print(czyUlozona(lista))
    print("ulozona dolna scianka")
    mc.postToChat("ulozona dolna scianka")
    pokaz(lista)
    if czyUlozona(lista):
        return "Udalo sie"
    sleep(5)
    lista = orientacjaOstatniejWarstwy(lista)
    print(czyUlozona(lista))
    print("zorientowana gorna scianka")
    mc.postToChat("zorientowana gorna scianka")
    pokaz(lista)
    if czyUlozona(lista):
        return "Udalo sie"
    sleep(5)
    lista = ustawWarstwe(lista)
    print(czyUlozona(lista))
    print("obrocona gorna scianka")
    mc.postToChat("obrocona gorna scianka")
    pokaz(lista)
    if czyUlozona(lista):
        return "Udalo sie"
    sleep(5)
    lista = permutacjaOstatniejWarstwy(lista)
    print(czyUlozona(lista))
    print("spermutowana gorna scianka")
    mc.postToChat("spermutowana gorna scianka")
    pokaz(lista)
    if czyUlozona(lista):
        return "Udalo sie"
    print("a tego nigdy nie powinno byc")
    mc.postToChat("a tego nigdy nie powinno byc")
    pokaz(lista)
    
print(ukladaj())
