'''Ler um número e calcular o fatorial'''

n = int(input('Digite um número para obter o fatorial: '))
c = n
f = 1
while c > 0:
    if c != 1:
        print(f'{c} x')
    else:
        print('{c} =')
    f *= c
    c -= 1
print(f'{f}.')