# Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo manter o programa correto, totalizando e contando os valores diferentes de zero que forem digitados.

# soma = 0
# A = 1

# while A != 0:
#    A = int(input("Digite X: "))
#    if A != 0:
#        soma = soma + A

# print(f'Soma dos valores = {soma}')

soma = 0
A = 1

while True:
    A = int(input("Digite X: "))
    soma += A
    if A == 0:
        break

print(f'Soma dos valores = {soma}')
