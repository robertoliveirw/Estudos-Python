'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Camp. Brasilieiorop de Futebol na ordem de colocação. Depois mostre.
A - Apenas os 5 primeiros
B - Os 4 últimos
C - Uma lista dos times em ordem afabética
D - Em qual posição na tabela está o time Red Bull Bragantino
'''
# Tabela 2024
contagem = 0 
times = (
    'Botafogo', 
    'Palmeiras', 
    'Flamengo', 
    'Fortaleza', 
    'Internacional', 
    'São Paulo', 
    'Corinthians', 
    'Bahia', 
    'Cruzeiro', 
    'Vasco', 
    'Vitória', 
    'Atlético-MG', 
    'Fluminense', 
    'Grêmio', 
    'Juventude', 
    'Red Bull Bragantino', 
    'Athletico-PR', 
    'Criciúma', 
    'Atlético-GO', 
    'Cuiabá'
)

print(f'Os 5 primeiros da tabela são: {times[:5]}')
print(f'Os 4 últimos da tabela são: {times[-4:]}')
print(f'A tupla em ordem alfabética é: {sorted(times)}')
for time in times:
    contagem += 1
    if time == 'Red Bull Bragantino':
        print(f'O time Red Bull Bragantino está na {contagem}º posição.')