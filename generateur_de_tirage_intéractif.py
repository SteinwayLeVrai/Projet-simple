import random

numero_simple = []
numero_etoile = []

random.seed(random.randint(1, 1000))

while len(numero_simple) < 5:
    tirage_simple = random.randint(1, 50)
    if tirage_simple not in numero_simple:
        numero_simple.append(tirage_simple)    

while len(numero_etoile) < 2:
    tirage_etoile = random.randint(1,12)
    if tirage_etoile not in numero_etoile:
        numero_etoile.append(tirage_etoile)
        
jeu = input("Entrée vos numero de 1 a 50: ").split()
jeu = [int(num) for num in jeu]

jeu_etoile = input("Entrée vos numero de 1 a 12: ").split()
jeu_etoile = [int(num) for num in jeu_etoile]

if any(num > 50 or num < 1 for num in jeu) or any(num > 12 or num < 1 for num in jeu_etoile):
    print("Vos numéros ne sont pas valides.")
elif jeu == numero_simple and jeu_etoile == numero_etoile:
    print("Vous avez gagné")
else:
    print("Vous avaient perdu")

   
print("Resultat: ", numero_simple)
print("Resultat etoile: ",numero_etoile)






