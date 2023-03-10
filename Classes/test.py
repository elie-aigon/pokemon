import random
def formule(lvl, att, defense, stab):
    print((((((lvl * 2)//5) + 2) * att * att //50 // defense) * random.randint(1, 5)) * stab)

formule(1, 52, 65, 0.5)
formule(1, 48, 58, 2)