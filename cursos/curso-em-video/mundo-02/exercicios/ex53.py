'''Ler uma frase e dizer se ela é um palindromo'''

frase = str(input('Digite a palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print(junto)
inverso = junto[::-1]
if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo')