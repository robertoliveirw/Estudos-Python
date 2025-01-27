# Laço While 
lista = []
r = 'S'

while r == 'S':
    n = str(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar [S/N]? : ')).upper()
print(lista)
print('FIM')
