"""
Énoncé. Affiche la table de multiplication de 1 à 10 pour un nombre donné par l’utilisateur.
"""
n = int(input("Nombre: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
