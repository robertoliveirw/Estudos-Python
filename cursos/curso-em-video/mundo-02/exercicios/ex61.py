'''Fazer o desafio 51 com while'''

'''pt = int(input('Digite o início: '))
razao = int(input('Digite o passo: '))
decimotermo = pt + (10-1)*razao

for c in range(pt, decimotermo, razao):
    print(c)'''

p = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o passo: '))
termo = p
c = 1
while c <= 10:
    print(f'{termo} ➡ ')
    termo += razao
    c += 1
print('FIM')