'''Refazer os exercícios 35 e dizer o tipo de triangulo que será formado 
- equilatero 
- Isosceles
- Esaleno'''

r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print("As três retas podem formar um triângulo EQUILÁTERO.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("As três retas podem formar um triângulo ISÓSCELES.")
    else:
        print("As três retas podem formar um triângulo ESCALENO.")
else:
    print("As três retas NÃO podem formar um triângulo.")
