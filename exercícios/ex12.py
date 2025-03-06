# Escreva uma função que conte o número de vogais em uma frase ou palavra.

# Função
def contar_vogais(string):
    vogais = 'AEIOU'
    return sum(1 for letra in string if letra in vogais)

frase = input('Digite uma frase:').upper()
print(contar_vogais(frase))