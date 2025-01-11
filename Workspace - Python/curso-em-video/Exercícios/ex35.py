# ler o comprimento de 3 retas e dizer se pode ou não fazer um triangulo

r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))

# Verifica se forma um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As três retas podem formar um triângulo.")
else:
    print("As três retas NÃO podem formar um triângulo.")
