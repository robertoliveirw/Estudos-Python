# Implemente uma calculadora que receba dois números e o tipo de operação (+, -, *, /) e exiba o resultado.

numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número:'))

operacao = int(input('Digite o dígito da operação a ser realizada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiiplicação \n 4 - Divisão \n'))

if operacao == 1:
    print('Você escolheu 1 - Soma')
    resultado = numero1 + numero2
    print('O valor da soma é: ', resultado)
elif operacao == 2:
    print('Você escolheu 2 - Subtração')
    resultado = numero1 - numero2
    print('O valor da Subtração é: ', resultado)
elif operacao == 3:
    print('Você escolheu 3 - Multiiplicação')
    resultado = numero1 * numero2
    print('O valor da Multiplicação é: ', resultado)
elif operacao == 4:
    print('Você escolheu 4 - Divisão')
    resultado = numero1 / numero2
    print('O valor da Divisão é: ', resultado)