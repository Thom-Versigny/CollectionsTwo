list={}
doorgaan='j'
while doorgaan=='j':
    product = input('wat voor product wilt u toevoegen: ')
    aantal = int(input('hoeveel wilt u dat product hebben: '))
    if product in list:
        list[product] += aantal
    else:
        list[product] = aantal
    doorgaan = input('wilt u nog meer producten toevoegen J/N: ').lower()
print(list)