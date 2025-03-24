# Tuplas são imutáveis

tupla = ('Roberto', 'Ricardo', 'Renato', 'Robson')

print(tupla)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])

print(tupla[1:3])

for indice in tupla:
    print(f'O nomé é: {indice}')