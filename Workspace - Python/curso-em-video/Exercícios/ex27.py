# ler o nome completo de uma pessoa, mostrar o primeiro e último nome
# O strip é para eliminar espaços antes e dps
nome = str(input('Qual o seu nome completo? \n')).strip()

listanome = nome.split()
primeironome = listanome[0]
ultimonome = listanome[-1]

print(f"Primeiro nome: {primeironome}")
print(f"Último nome: {ultimonome}")

# Finalizado
