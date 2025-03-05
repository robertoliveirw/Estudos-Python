# Calcule o fatorial de um número informado pelo usuário usando um loop.

numero = int(input('Digite um número:'))
controlador = 1

for numeros in range(1, numero+1):
    print(numeros)
    controlador *= numeros
    
print(f'O fatorial é: {controlador}')