# Exemplos de operações com conjuntos em Python

# Conjuntos para os exemplos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Diferença (A - B)
diferenca = A - B
print(f"Diferença (A - B): {diferenca}")

# 2. União (A | B)
uniao = A | B
print(f"União (A | B): {uniao}")

# 3. Interseção (A & B)
intersecao = A & B
print(f"Interseção (A & B): {intersecao}")

# 4. Diferença Simétrica (A ^ B)
diferenca_simetrica = A ^ B
print(f"Diferença Simétrica (A ^ B): {diferenca_simetrica}")

# 5. Pertence (valor in A)
valor = 2
pertence = valor in A
print(f"O valor {valor} pertence ao conjunto A? {pertence}")

# 6. Não Pertence (valor not in A)
valor = 5
nao_pertence = valor not in A
print(f"O valor {valor} não pertence ao conjunto A? {nao_pertence}")
