# Estruturas condicionais

# Estrutura 01
tempo = float(input('Quantos anos tem o seu carro? '))
if tempo >= 5:
    print('Carro Velho')
else:
    print('Carro Novo')

# Estrutura 02

print('Carro Velho'if tempo >= 5 else 'Carro Novo')

# Estutura 03

if tempo > 10:
    print('Carro Velho')
elif tempo >= 5 and tempo < 10:
    print('Carro Meia-vida')
elif tempo < 5:
    print('Carro Novo')
