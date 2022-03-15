import random
kaart=["schoppen", "harten", "klarven", "ruiten"]
deck = []
for aantal in range(2,11):
    for x in kaart:
        deck.append(str(x)+' '+str(aantal))
for aantal in kaart:
    deck.append(str(aantal)+' vrouw')
    deck.append(str(aantal)+' boer')
    deck.append(str(aantal)+' aas')
for aantal in range(2):
    deck.append('joker')
random.shuffle(deck)
for x in range(1,8):
    print(f'kaart {x}: {deck.pop()}')
print(f'deck (47 kaarten): {deck}')