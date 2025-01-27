'''Ler 5 números e falar o maior e o menor'''

lista = []

for c in range(0,5):
    peso = float(input('Digite o peso: '))
    lista.append(peso)

maior = max(lista)
menor = min(lista)

print(f'O maior número é {maior} e o menor é {menor}')