# Um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiuculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (Desconsiderar espaço)
# Quantas letras tem o primeiro nome


nome = input('Qual o seu nome completo?')

maiusculo = nome.upper()
minusculo = nome.lower()
primeironome = nome.split()[0]
letrasprimeironome = len(primeironome)

print(maiusculo)
print(minusculo)
print(primeironome)
print(letrasprimeironome)
