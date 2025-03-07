# Dada uma lista com números (ou strings), remova os elementos duplicados.

from random import randint

def geradordelista(qtde):
    L = []
    for i in range(qtde):
        L.append(randint(1, 5))
    return L

qtde_de_itens = int(input('QUANTIDADE DE NÚMEROS DA LISTA'))

lista_original = geradordelista(qtde_de_itens)
print('A lista original é: ', lista_original)

lista_sem_duplicados = sorted(set(lista_original))
print('A lista sem duplicados é: ', lista_sem_duplicados)