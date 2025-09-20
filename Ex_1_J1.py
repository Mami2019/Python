"""
Ex1
Énoncé. Demande le prénom et l’âge de l’utilisateur, puis affiche :
Bonjour <prénom>, tu as <âge> ans.
Affiche ensuite : L’an prochain, tu auras <âge+1> ans.
"""
prenom = input("Tom prénom? ")
age = int(input("Ton age? "))
print(f"Bonjour {prenom}, tu as {age} ans.")
print(f"L'an prochain, tu auras {age + 1} ans.")