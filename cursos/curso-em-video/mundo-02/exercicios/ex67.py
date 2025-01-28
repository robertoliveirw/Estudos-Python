'''Faça um programa que mostre a tabuada de vários números um de cada vez para cada valor digitado. O programa será interrmopido quando um número negativo for solicitado'''
while True:
    numero = int(input("Digite um número: \n"))
    print(f"Tabuada do {numero}:")
    
    if numero < 0:
        print('Programa encerrado!')
        break

    for c in range(0, 11):
        nn = numero*c
        print(f'{numero} x {c} = {nn}')