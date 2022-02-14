list={}
doorgaan='j'
while doorgaan=='j':
    product = input('wat voor product wilt u toevoegen: ')
    aantal=input('hoeveel wilt u dat product hebben: ')
    doorgaan = input('wilt u nog meer producten toevoegen J/N: ').lower()
    list[product] = aantal
print(list)
