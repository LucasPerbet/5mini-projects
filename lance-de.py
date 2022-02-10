import random
print("Appuyer sur  1 pour lancé le Dé")
print("Appuyer sur 0 pour quitter")
while True:
    # On demande à l'utilisateur de taper sur un nombre de son clavier
    x = int(input('Appuyer sur votre clavier pour lancer le Dé'))
    if x == 0:
        print("A bientôt")
        break

    elif x == 1:
        print(random.randint(1, 6))
    else:
        print("Appuyer sur 1 pour lancer ou 0 pour quitter")
