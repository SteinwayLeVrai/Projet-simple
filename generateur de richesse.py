import random

numero_simple = []
numero_etoile = []

random.seed(random.randint(1, 1000))

while len(numero_simple) < 5:
    tirage_simple = random.randint(1, 50)
    if tirage_simple not in numero_simple:
        numero_simple.append(tirage_simple)
    
print(numero_simple)

while len(numero_etoile) < 2:
    tirage_etoile = random.randint(1,12)
    if tirage_etoile not in numero_etoile:
        numero_etoile.append(tirage_etoile)
        
print(numero_etoile)







