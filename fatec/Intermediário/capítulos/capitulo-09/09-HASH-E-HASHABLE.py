# Definição de strings e cálculo de hash
s1 = 'texto'
print(hash(s1))

s2 = 'qualquer coisa'
print(hash(s2))

# Definição de um valor float e cálculo de hash
valor = 13.75
print(hash(valor))

# Definição de inteiros e cálculos de hash
x = 26
print(hash(x))

y = 26.0
print(hash(y))

# Definição de tupla e cálculo de hash
t = (15, 23, 7)
print(hash(t))

# Definição de lista e tentativa de cálculo de hash
l = [15, 23, 7]
# print(hash(l))  # Gera TypeError: unhashable type: 'list'
