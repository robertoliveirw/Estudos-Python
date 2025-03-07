# Inverta os elementos de uma lista sem usar métodos prontos.
from random import randint

def geradordelista(qtde):
    L = []
    for i in range(qtde):
        L.append(randint(1, 10))
    return L

qtde_de_itens = int(input('QUANTIDADE DE NÚMEROS DA LISTA: '))

lista_original = geradordelista(qtde_de_itens)
lista_invertida = lista_original[::-1]

print('A lista original é: ', lista_original)
print('A lista invertida é: ', lista_invertida)