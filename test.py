games = ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']
punten=0
for i in range(len(games)):
    number= games[i]
    x = number.split(':')
    endstand = [int(item) for item in x]
    if x[0]==x[1]:
        punten+=1
    elif x[0] > x[1]:
        punten += 3

print(punten)
