'''Exemplo 13.1'''
lista = [31, -17, 26, 15, -35, -9, 20]

# Modo convencional:
modo1 = []
for i in lista:
    modo1.append(i*2)
print(modo1)

# Atraves da compressão de lista
modo2 = [x*2 for x in lista]
print(modo2)