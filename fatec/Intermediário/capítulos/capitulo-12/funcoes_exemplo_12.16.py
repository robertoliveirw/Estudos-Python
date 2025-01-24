# Exemplo 12.16
'''Função  Lambda'''

# Função Criada
def Fatorial(N):
        if N <= 1:
            return 1 
        else:
              return N * Fatorial(N-1)
# Código Principal

entrada = int(input('Digite um número:'))
F = Fatorial(entrada)
print(f'O fatorial de {entrada} é {F}')