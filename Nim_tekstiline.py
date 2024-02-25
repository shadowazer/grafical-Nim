from random import choice
seis = [3, 5, 7, 2]
number=2
pik=8

def seis2bitijada(seis):
    tulemus=[]
    for x in seis:
        tulemus.append(bitijada(x))
    return tulemus

def kasvoiduseis(seis):
    kahendsusteem = seis2bitijada(seis)
    summad=[]
    for pos in range(pik):
        summa = 0
        for jada in kahendsusteem:
            summa += jada[pos]
        summad.append(summa%2)
    return max(summad)==1    

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
        if summa%2 == 1:
            a = a if a is not None else choice(uhed)
            kahendsusteem[a][pos] = 1 - kahendsusteem[a][pos]
    return [list(reversed(x)) for x in kahendsusteem]    
    #  [int(''.join(str(a) for a in x), 2) for x in kahendsusteem]

def leiakaik(seis):
    if kasvoiduseis(seis):
        kaik = kaiguleidmine(seis)
        tulemus2 = []
        for x in kaik:
            num=0
            for i in range(pik):
                num+=x[i]*(2**i)
            tulemus2.append(num)    
        return tulemus2
    # kuna pole võiduseis, võta 1 suurimast reast
    tulemus2 = list(seis)
    suurim = max(tulemus2)
    tulemus2[tulemus2.index(suurim)] -= 1
    return tulemus2
    

def bitijada(arv):    
    tulemus=[]
    for i in range(pik):
        tulemus.append(arv%2)
        arv=arv//2
    return tulemus

def Seis(seis):
    for i in range(len(seis)):   
        print(i+1, end=") ")
        for j in range(seis[i]):
            print("*", end = "")
        print("")

Seis(seis)

def kontrolli_kaiku(rida, sammud):
    if rida <= len(seis) and rida > 0 and sammud <= seis[rida-1] and sammud > 0: 
        return False
    print("sisestatud käik ei ole korrektne")
    return True

mang_kaib = True
while mang_kaib:
    kaik = True
    print("mängija "+str(number))
    if number == 1:
        seis = leiakaik(seis)
    else:
        while kaik:
            try:
                rida = int(input("rida: "))
                sammud = int(input("sammude arv: "))
                kaik = kontrolli_kaiku(rida, sammud)
            except ValueError:
                print("Vigane sisend")

        #käigu teostus
        seis[rida-1] -= sammud
    Seis(seis)
    if max(seis) == 0:
        mang_kaib = False
        print("mängija "+ str(number) + " võitis")
    if number == 1:
        number = 2
    else:
        number = 1
    