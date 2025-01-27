'''Ler o ano de nascimento de uma pessoa e retornar:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou o tempo de Alistamento

Deve mostrar o tempo que falta ou o tempo que passou'''

ano = int(input('Qual ano você nasceu? '))
idade = 2025 - ano

if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    f_idade = 18 - idade
    print(f'Não está na hora de se alistar! \nFaltam {f_idade} anos.')
else:
    f_idade = idade - 18
    print(f'Você já passou da hora de se alistar! \nEstá {f_idade} anos atrasado!.')