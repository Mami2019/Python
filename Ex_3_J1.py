"""
Ex3:
Énoncé. Demande un nombre de minutes (entier).
Affiche le même temps au format Hh Mm (ex. 135 → 2h 15m).
"""
nb_minutes = int(input("Nombre de minutes: "))
heure =  nb_minutes // 60
minutes = nb_minutes % 60

print(f"il est {heure} : {minutes}")

"""
Pour aller plus loin (optionnel)
Tester type(variable) pour voir le type.
Essayer des entrées “invalides” (ex. âge = "abc") et observer l’erreur.
"""