# Exemplo 12.5
from random import randint

# Função Criada
def geradordelistas(qtd):
    '''Carrega uma lista com QTD numeros inteiros aleatórios'''
    L = []
    for i in range(qtd):
        L.append(randint(1,10000))
    return L
    

# Código Principal
valores = int(input('Digite a quantidade de itens na lista: '))
lista = geradordelistas(valores)
print(f'Lista gerada >> {lista}')