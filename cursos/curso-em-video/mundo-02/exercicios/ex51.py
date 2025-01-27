'''Ler o primeiro termo e a razão de uma PA e motrar os 10 primeiros termos'''

pt = int(input('Digite o início: '))
razao = int(input('Digite o passo: '))
decimotermo = pt + (10-1)*razao

for c in range(pt, decimotermo, razao):
    print(c)