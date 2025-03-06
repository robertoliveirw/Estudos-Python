# Crie um programa que ordene uma lista de números em ordem crescente.
from random import randint

# Função 

def geradordelista(qtde, limite_inferior, limite_superior):
    lista = []
    for i in  range(qtde):
        lista.append(randint(limite_inferior, limite_superior))
    return lista

qtd_valores = int(input('DIGITE A QUANTIDADE DE NÚMEROS DA LISTA:'))
int_inferior = int(input('DIGITE O INTERVALO INFERIOR DE NÚMEROS DA LISTA:'))
int_superior = int(input('DIGITE O INTERVALO SUPERIOR DE NÚMEROS DA LISTA:'))

lista_atual = geradordelista(qtd_valores, int_inferior, int_superior)
lista_ordenada = sorted(lista_atual)

print(f'Lista gerada {lista_atual} \n Lista ordenada {lista_ordenada}')