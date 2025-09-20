"""
Énoncé. Demande un mot de passe. Si c’est "python123", affiche “Accès autorisé”, sinon “Accès refusé”.
"""
mdp = input("Mon de passe : ")
if mdp == "python123":
    print("Accès autorisé")
else:
    print("Accès refusé")