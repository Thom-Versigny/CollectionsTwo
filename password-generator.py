import random
import string
letters = string.ascii_lowercase
hooftletters = string.ascii_uppercase
getal = string.digits
speciale = ['@', '#', '$', '%', '&', '_' ,'?']

def wachtwoord():
    password = []
    for i in range(random.randint(2,6)):
        password.append(random.choice(hooftletters))
    for i in range(3):
        password.append(random.choice(speciale))
    for i in range(random.randint(4, 7)):
        password.append(random.choice(getal))
    x = 24 - len(password)
    for i in range(x):
        password.append(random.choice(letters))
    random.shuffle(password)
    while (password[0] in speciale or password[0] in getal or password[1] in getal or password[2] in getal or password[23] in speciale):
         random.shuffle(password)
    return ''.join(password)

password = wachtwoord()
print(password)

