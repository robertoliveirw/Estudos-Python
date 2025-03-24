'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra quais são as suas vogais
'''

tupla = (
        'Amaciante',
        'Costa',
        'Peito'
        )

vogais = 'AEIOU'
for palavra in tupla:
    palavra = palavra.upper()
    vogais_palavra = ()
    for letra in palavra:
        if letra in vogais:
            vogais_palavra += (letra,)  
    print(f'A palavra {palavra} possui as vogais: {", ".join(vogais_palavra)}')