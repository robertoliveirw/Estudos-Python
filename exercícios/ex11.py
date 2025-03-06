# Verifique se uma string é um palíndromo (lê-se igual de trás para frente).

'''string1 = 'oi'
string2 = 'io'
string2_invertida = string2[::-1]

if string2_invertida == string1:
    print('Palíndromo')
else:
    print('Não é palíndromo')'''

string = input('Digite um texto para verificar se é palíndromo:')
invertida = string[::-1]

if string == invertida:
    print('Palíndromo')
else:
    print('Não é palíndromo') 