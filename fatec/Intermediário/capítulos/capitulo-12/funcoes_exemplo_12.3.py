# Exemplo 12.3

from random import randint

# Função Criada
def geradordelistas():
    L = []
    for i in range(10):
        L.append(randint(1,10000))
    return L

# Código Principal
valores = geradordelistas()
print(f'Lista gerada >> {valores}')

