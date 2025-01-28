'''Caixa eletrônico - Valor a ser sacado (int) e o programa deverá informar quantas cédulas serã entregues

O caixa possui cédulas de 50, 20, 10 e 1'''

print('='*30)
print('{:^30}'.format('ATM'))
print('='*30)

valor = int(input('Quantia a ser sacada: '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


