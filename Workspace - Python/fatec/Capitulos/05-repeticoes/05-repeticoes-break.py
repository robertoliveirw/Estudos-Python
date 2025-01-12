# Posso para o programa de uma vez utilizando o Break.

i = 1

while True:
    i = int(input('Digite um número: \n'))
    if i == 0:
        break
    print(i, end=' ')

print('Fim do programa')
