'''Melhorar o ex anterior perguntando quantos termos a mais deseja mostrar, se for 0 terminar o programa '''

n = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = n
c = 1
p = 10
tot = 0
while p != 0:
    tot += p
    while c <= tot:
        print(f'{termo} ➡ ')
        termo += razao
        c += 1
    print('PAUSA')
    p = int(input('Quantos termos quer mostrar a mais? '))
print(f'\nA progressao foi finalizada com {c} termos mostrados.')