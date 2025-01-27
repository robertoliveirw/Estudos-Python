'''Calcular a soma entre todos os numeros impares que são multiplos de 3 entre 1 e 500'''

n=0
cont = 0

for c in range (1, 501,2):
    if c % 3 == 0:
        cont += 1
        n+= c
print(f'A soma de todos os {cont} valores é {n}')