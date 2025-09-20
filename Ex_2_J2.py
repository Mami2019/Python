"""
Énoncé. Lis deux nombres et un opérateur (+ ou -) puis affiche le résultat.
"""
a = int(input("Nombre1 : "))
b = int(input("Nombre2 : "))
op = input("Opérateur (+ ou -) : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print("Opérateur inconnu")