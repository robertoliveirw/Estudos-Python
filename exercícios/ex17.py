# Encontre o maior e o menor número em uma lista.
from random import randint

# Função

def geradordelista(qtde, limite_inferior, limite_superior):
    lista = []
    for i in range(qtde):
        lista.append(randint(limite_inferior, limite_superior))
    return lista

qtd_valores = int(input('DIGITE A QUANTIDADE DE NÚMEROS DA LISTA:'))
int_inferior = int(input('DIGITE O INTERVALO INFERIOR DE NÚMEROS DA LISTA:'))
int_superior = int(input('DIGITE O INTERVALO SUPERIOR DE NÚMEROS DA LISTA:'))

lista_gerada = geradordelista(qtd_valores, int_inferior, int_superior)
menor_valor = min(lista_gerada)
maior_valor = max(lista_gerada)

print(f'A lista é: {lista_gerada} \n Quantidade de itens na lista: {qtd_valores}\n Limite Superior: {int_inferior} \n Limite Inferior: {int_superior} \n Menor Valor: {menor_valor} \n Maior Valor: {maior_valor}')
