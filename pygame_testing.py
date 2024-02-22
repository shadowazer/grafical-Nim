import time
from random import choice
import pygame
from pygame.locals import *
import sys
import random
seis = []
clickcords = []


pik = 8

def seis2bitijada(seis):
    tulemus = []
    for x in seis:
        tulemus.append(bitijada(x))
    return tulemus

def kasvoiduseis(seis):
    kahendsusteem = seis2bitijada(seis)
    summad = []
    for pos in range(pik):
        summa = 0
        for jada in kahendsusteem:
            summa += jada[pos]
        summad.append(summa % 2)
    return max(summad) == 1

def kaiguleidmine(seis):
    kahendsusteem = [list(reversed(x)) for x in seis2bitijada(seis)]
    a = None
    for pos in range(pik):
        summa = 0
        uhed = []
        for i in range(len(kahendsusteem)):
            jada = kahendsusteem[i]
            if jada[pos] == 1:
                uhed.append(i)
            summa += jada[pos]
        if summa % 2 == 1:
            a = a if a is not None else choice(uhed)
            kahendsusteem[a][pos] = 1 - kahendsusteem[a][pos]
    return [list(reversed(x)) for x in kahendsusteem]
    #  [int(''.join(str(a) for a in x), 2) for x in kahendsusteem]

def leiakaik(seis):
    if kasvoiduseis(seis):
        kaik = kaiguleidmine(seis)
        tulemus2 = []
        for x in kaik:
            num = 0
            for i in range(pik):
                num += x[i] * (2 ** i)
            tulemus2.append(num)
        return tulemus2
    # kuna pole võiduseis, võta 1 suurimast reast
    tulemus2 = list(seis)
    suurim = max(tulemus2)
    tulemus2[tulemus2.index(suurim)] -= 1
    return tulemus2

def bitijada(arv):
    tulemus = []
    for i in range(pik):
        tulemus.append(arv % 2)
        arv = arv // 2
    return tulemus


def seisugeneraator(laius, pikkus):
    for l in range(laius):
        seis.append(random.randint(1, pikkus-1))

def korrektnekaik(selected, w, e):
     if w == selected[0] and 0 <= e and e < selected[1]:
         korrektne = True
     else:
         korrektne = False
     return korrektne




def main(laius, pikkus):
    global seis
    def ruuduleidja(clickcords):
        w = ((clickcords[0] - iluVahe) // ruuduKulg)
        e = (clickcords[1] - iluVahe2) // ruuduKulg
        return int(w), int(e)

    def nupujoonistus(i, n):
        x = iluVahe + i * ruuduKulg
        y = iluVahe2 + n * ruuduKulg
        laud.blit(nupp,(x, y))

    def ruudujoonistus(i, n):
        pygame.draw.rect(
            laud,
            clr1 if (i + n) % 2 == 0 else clr2,
            (iluVahe + i * ruuduKulg, iluVahe2 + n * ruuduKulg, ruuduKulg, ruuduKulg)
        )

    seisugeneraator(laius, pikkus)
    fps = 30
    aknakorgus = 640
    aknalaius = 720
    laualaius = aknalaius - 60
    lauakorgus = aknakorgus - 60

    ruuduKulg = int(min(laualaius / laius, lauakorgus / pikkus))
    iluVahe = (aknalaius - laius * ruuduKulg) / 2
    iluVahe2 = (aknakorgus - pikkus * ruuduKulg) / 2
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    aken = pygame.display.set_mode((aknalaius, aknakorgus))
    laud = pygame.Surface(aken.get_size())
    nupp_alg = pygame.image.load("nupp_1.png").convert_alpha()
    nupp = pygame.transform.scale(nupp_alg, (ruuduKulg, ruuduKulg))
    # tekstikast = pygame.draw.rect(laud, (255, 255, 255), (300, 620, 100, 15))
    clr1 = "aquamarine3"
    clr2 = "azure3"
    for n in range(pikkus):
        for i in range(laius):
            ruudujoonistus(i, n)
            if n == seis[i]:
                nupujoonistus(i, n)

    aken.blit(laud, (0, 0))
    pygame.display.flip()
    tmer = None
    selected = None
    selected1 = None
    number = 1
    hide = True
    run = True
    kas_vajutatud = False
    event = None
    while run:
        FPSCLOCK.tick(fps)
        event_list = pygame.event.get()
        for event in event_list:
            if event is not None and event.type == pygame.QUIT:
                run = False
            if number == 1:
                if kas_vajutatud == False and event.type == MOUSEBUTTONUP:
                    clickcords = pygame.mouse.get_pos()
                    w, e = ruuduleidja(clickcords)
                    if not 0 <= w < laius or not 0 <= e < pikkus:
                        continue
                    if e == seis[w]:
                        selected = (w, e)
                        tmer = 14
                        kas_vajutatud = True
                elif kas_vajutatud and event.type == MOUSEBUTTONUP:
                    clickcords = pygame.mouse.get_pos()
                    w, e = ruuduleidja(clickcords)
                    korrektne = korrektnekaik(selected, w, e)
                    if korrektne:
                        ruudujoonistus(*selected)
                        nupujoonistus(w, e)
                        seis[w] = e
                        if sum(seis) == 0:
                            #joonistus mängija... võitis
                            number = 0
                        else:
                            number = 2
                    else:
                        nupujoonistus(*selected)
                        selected = None
                    kas_vajutatud = False
                    tmer = None
                    hide = True

        if number == 2:
            seis = leiakaik(seis)
            print(seis)
            for n in range(pikkus):
                for i in range(laius):
                    ruudujoonistus(i, n)
                    if n == seis[i]:
                        nupujoonistus(i, n)
            if sum(seis) == 0:
                # joonistus mängija... võitis
                number = 0
            else:
                number = 1

        if tmer is not None:
            tmer += 1
            tmer = tmer % 15
            if kas_vajutatud and tmer == 0 and selected is not None:
                if hide:
                    ruudujoonistus(*selected)
                    hide = False
                else:
                    nupujoonistus(*selected)
                    hide = True
        aken.blit(laud, (0, 0))
        pygame.display.flip()
            # if event.type == MOUSEBUTTONUP:
            # pygame.draw.rect(laud, hele, (20, 30, 500, 100))
        # pygame.draw.rect(laud, hele, (20, 30, 50, 50))
        # aken.blit(laud, (0, 0))
        # pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
