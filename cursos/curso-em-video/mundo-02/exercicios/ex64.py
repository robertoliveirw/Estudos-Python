'''Ler vários números inteiros e parar com 999. No final mostrar a soma entre eles e desconsiderando o 999'''

c = 0
num = 0
while num != 999:
    num = int(input('Digite um número: '))
    c += num

nnum = c - 999

print(nnum)