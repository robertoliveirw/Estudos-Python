# Exemplo 12.10
'''Desempacotamento de dados com tupla'''
# Função Criada

def desempacotamento (a,b,c):
    return (a + b) / c

# Código Principal

L1 = [12, 20, 5] # Neste caso funciona pq a quantidade de itens na lista é a mesma que foi criada na função.
A = desempacotamento(*L1)
print(A)

