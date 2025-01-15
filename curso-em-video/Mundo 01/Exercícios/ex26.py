# Verificar quantas vezes aparece a letra A, em que posição aparece a primeira e última vez

frase = str(input('Digite uma palavra ou frase: \n')).upper()
# O .upper está com a finalidade de deixar tudo em maiúsculo para não haver diferença na contagem entre a e A
numerodevezes = frase.count('A')
print(f'A letra \"A\" aparece {numerodevezes} vezes na frase.')
primeiraposicao = frase.find('A')+1
print(f'A letra \"A\" aparece na posição {primeiraposicao} pela primeira vez.')
ultimaposicao = frase.rfind('A')+1
print(f'A letra \"A\" aparece na posição {ultimaposicao} pela última vez.')
