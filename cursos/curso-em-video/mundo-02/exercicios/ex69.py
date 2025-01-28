'''Ler idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deve perguntar se o usuário quer ou nao continuar. Mostrar no final:

Pessoas com mais de 18 anos
Quantas mulheres cadastradas
Quantas mulheres tem menos de 20 anos'''

total_maior_18 = 0 
mulheres = 0
mulheres_menor20 = 0
pessoas = 0

while True:
    idade = int(input('Digite a Idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = input('Digite o sexo [M/F]: ').strip().upper()[0] # O [0] é para pegar apenas a primeira letra da string
    # Contagem de pessoas cadastradas:
    pessoas += 1

    
    # Verifica maior de 18 anos
    if idade > 18:
        total_maior_18 += 1
    
    # Verifica mulheres cadastradas
    if sexo in 'F':
        mulheres += 1
 
    # Verifica mulheres cadastradas com menos de 20 anos
    if sexo in 'F' and idade < 20:
        mulheres_menor20 += 1    
    
    # Perguntar se quer continuar
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total_maior_18}')
print(f'Total de mulheres cadastradas: {mulheres}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {mulheres_menor20}')
print(f'Total de pessoas cadastradas: {pessoas}')
print('Fim')