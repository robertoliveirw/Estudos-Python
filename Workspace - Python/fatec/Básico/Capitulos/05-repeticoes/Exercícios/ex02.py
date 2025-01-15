# Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis por 7 entre 1 e N (inclusive).

n = int(input('Digite um número: \n'))
i = 1

while i <= n:
    if i % 7 == 0:
        print(i)
    i += 1
print('Programa Finalizado')
