'''Refazer o ex09 mostrando a taubada de um número que o usuário escolher só que agora usando o laço for'''

# Tabuada
numero = int(input("Digite um número: \n"))
print(f"Tabuada do {numero}:")

for c in range(0, 11):
    nn = numero*c
    print(f'{numero} x {c} = {nn}')
