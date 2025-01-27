'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão 
1 - Binário
2 - Octal
3 - Hexadecimal'''

numero = int(input('Digite um número: '))
escolha = int(input('Você deseja transformar o número inteiro para: 1 - Binário | 2 - Octal | 3 - Hexadecimal:' ))

if escolha == 1:
    binario = bin(numero)  # Converte para binário
    print(f'O numero {numero} em Binário é: {binario}')
elif escolha == 2: 
    octal = oct(numero)  # Converte para octal
    print(f'O numero {numero} em Octal é: {octal}')
elif escolha == 3:
        hexadecimal = hex(numero)
        print(f'O número {numero} em Hexadecimal é: {hexadecimal}')
else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
