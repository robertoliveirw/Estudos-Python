# Comando macth case

n = -1 

while n != 0:
    
    n = int(input('Digite um número inteiro de 1 a 5. Caso digite \'0\' o programa será encerrado!'))

    match n:
        case 1:
            print('Um')
        case 2:
            print('Dois')
        case 3:
            print('Três')
        case 4:
            print('Quatro')
        case 5:
            print('Cinco')
        case _:
            print('Inválido')

print('Programa encerrado!')
    
