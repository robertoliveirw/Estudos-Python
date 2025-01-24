# Exemplo 12.10
'''Função  Recursiva (Chamar ela mesmo dentro dela)'''

# Função Criada
def Fatorial(N):
        if N <= 1:
            return 1 
        else:
              return N * Fatorial(N-1)