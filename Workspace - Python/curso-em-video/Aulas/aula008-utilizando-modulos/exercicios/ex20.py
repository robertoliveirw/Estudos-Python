# o mesmo professor quer sortear uma ordem para os alunos apresentarem o trabalho, sorteie esta ordem.
import random

a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')

lista = [a1, a2, a3, a4]

random.shuffle(lista)  # Deixa a ordem da lista embaralhada
print('Os alunos sorteados são: ')
print(lista)
