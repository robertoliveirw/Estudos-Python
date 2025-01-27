'''Ler 6 numeros inteiros e mostrar a soma apenas dos numeros pares'''

par = 0
cont = 0 
for c in range(0,6):
    n = int(input('Digite um número: '))
    if c % 2 == 0:
        par+= n
        cont += 1
print(f'Você informou {cont} números pares, a soma dos números pares é {par}')