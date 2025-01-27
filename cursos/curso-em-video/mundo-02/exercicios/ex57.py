'''Fazer um programa que só aceite M ou F para o sexo'''

sexo = 'string aleatória'

while sexo not in 'MnFf':
    sexo = str(input('Digite o sexo [M/F]')).upper().strip()  
    if sexo == 'M':
        print('Seu sexo é Masculino')
    elif sexo == 'F':
        print('Seu sexo é Feminino')
    else:
        print('Escolha inválida!')