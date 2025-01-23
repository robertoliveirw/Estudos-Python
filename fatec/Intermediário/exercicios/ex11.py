'''Exercício resolvido número 11 referente ao exercício: Resolvido 12.1
Escreva um programa que leia dois números reais e calcule as 4 operações aritméticas entre eles usando uma função. Exiba o resultado com duas casas decimais. '''

def operacoes(a,b):
    adicao = a + b
    print(f'O resultado da soma é: {adicao}')
    subtracao = a - b
    print(f'O resultado da subtracao é: {subtracao}')
    multiplicacao = a * b
    print(f'O resultado da multiplicacao é: {multiplicacao}')
    divisao = a / b
    print(f'O resultado da divisao é: {divisao}')
    return adicao, subtracao, multiplicacao, divisao

V1 = int(input('Digite o primeiro número: '))
V2 = int(input('Digite o segundo número: '))

resultado = operacoes(V1,V2)
