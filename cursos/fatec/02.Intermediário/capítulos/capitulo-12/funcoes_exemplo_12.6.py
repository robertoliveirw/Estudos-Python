# Exemplo 12.6
from random import randint

# Função Criada
def geradordelistas(qtd, a, b):
    '''Carrega uma lista com uma QTD aleatório e os parâmetros entre o número mínimo e máximo fornecido pelo usuário.'''
    L = []
    for i in range(qtd):
        L.append(randint(a,b))
    return L

# Código Principal
valores = int(input('Digite a quantidade de itens na lista: '))
lmin = int(input('Qual o intervalo inferior da lista: '))
lmax = int(input('Qual o intervalo superior da lista: '))
lista = geradordelistas(valores, lmin, lmax)
print(f'Lista gerada >> {lista}')