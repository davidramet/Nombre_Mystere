import random

#GENERER LE NOMBRE ALEATOIRE
nombreAleatoire = random.randint(1,100)
nombreAleatoire = str(nombreAleatoire)
print(nombreAleatoire)

#DEMANDE A UTILISATEUR UN NOMBRE
solution=input("Veuillez saisir un nombre : ")

#BOUCLE TANT QUE LE JOUEUR A PAS TROUVE
while solution!=nombreAleatoire:
  if solution>nombreAleatoire:
    print("Trop grand")
  else:
    print("Trop petit")
  solution=input("Veuillez saisir un nombre : ")
print("VOUS AVEZ TROUVE LE BON NOMBRE !")
