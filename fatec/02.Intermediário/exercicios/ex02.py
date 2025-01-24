codigos = [1,2,3,4,5,6,7,8,9,10]
lista = []

for codigo in codigos:
    lista.append(codigo) if codigo >= 2 and codigo <= 8 else 0;
print(lista)