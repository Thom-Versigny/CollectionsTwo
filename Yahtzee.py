import random
over=5
houden = []
dobbelcijfers = [1,2,3,4,5,6]
def gooien():
    global over
    gegooit = []
    for x in range(over):
        gegooit.append(random.choice(dobbelcijfers))
    while True:
        print(gegooit)
        if input('wilt u dobbelstenen houden? j/n: ').lower()=='n':
            over = len(gegooit)
            return houden
        else:
            keuze = int(input('welk dobbelsteen wilt u houden? '))
            houden.append(gegooit[keuze-1])
            gegooit.pop(keuze-1)

gooien()
print(houden)
