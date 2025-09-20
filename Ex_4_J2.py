"""
Énoncé. Lis une note sur 20 et affiche :
Échec si < 10
Passable si entre 10 et 12
Bien si entre 12 et 16
Très bien si ≥ 16
"""
note = float(input("Ta note : "))
if note < 10:
    print("Echec")
elif note >= 10 and note < 12:
    print("Passable")
elif note >=12 and note < 16:
    print("Bien")
else:
    print("très bien!")
