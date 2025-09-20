"""
Ex2:
Énoncé. Lis un montant HT (nombre) et un taux de TVA en pourcentage,
calcule et affiche le total TTC arrondi à 2 décimales.
"""
Mht = float(input("Montant hors taxe (Mht): "))
tva = float(input("tva en % : "))
Mtt = Mht * (1 + (tva / 100))

print(f"Le Montant TTC : {Mtt} €")