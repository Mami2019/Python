"""
Objectifs du jour
Comprendre la structure if / elif / else
Comparateurs (==, !=, <, <=, >, >=)
Combiner conditions avec and, or, not
Pratiquer des tests de base
"""
age = int(input("Äge : "))

if age < 18 :
    print("Mineur")
elif age < 65:
    print("Adulte")
else:
    print("Senior")

"""
note = 15
if note >= 10 and note <= 20:
    print("Réussi")
"""