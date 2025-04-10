lista = list()
for i in range(0,5):
    n = int(input('Digite um valor: '))
    lista.append(n)

print(f'A lista é: {lista}, o valor mínimo é {min(lista)}, posicionado no índice {lista.index(min(lista))}. O valor máximo é {max(lista)} posicionado no índice {lista.index(max(lista))}. ')
