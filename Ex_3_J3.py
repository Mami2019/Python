"""
Énoncé. Un nombre secret (par exemple 7) est fixé. Demande à l’utilisateur de deviner jusqu’à ce qu’il trouve. Affiche le nombre d’essais.
"""
secret = 7
essais = 0
while  True:
    n = int(input("Dévine le nombre : "))
    essais += 1
    if n == secret:
        print(f"Bravo! Trouvé en {essais} essais.")
        break
    else:
        print("Raté, essaie encore.")