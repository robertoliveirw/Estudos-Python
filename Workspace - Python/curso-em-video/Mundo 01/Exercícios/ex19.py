# Um professor quer sortear um dos seus 4 alunos para apgar o quadro. Faça um programa que sorteie um nome.
import random

a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')

lista = [a1, a2, a3, a4]

sorteio = random.choice(lista)
print(sorteio)
