import random
import string
characters = list(string.ascii_letters + string.digits + "@#$%&_?")
letters = string.ascii_lowercase
hooftletters = string.ascii_uppercase
getal = string.digits
speciale = ['@', '#', '$', '%', '&', '_' ,'?']

def wachtwoord():
    random.shuffle(characters)
    password = []
    for i in range(24):
	    password.append(random.choice(characters))
    
    print("".join(password))
    if password.count(speciale) == 0 or password.count(speciale) == 23:
        random.shuffle(password)
    else:
        if password.count(getal) == 0 or password.count(getal) == 1 or password.count(getal) == 2:
            random.shuffle(password)
        else:



