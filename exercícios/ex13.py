# Conte quantas vezes cada caractere aparece em uma string (use um dicionário para armazenar os resultados).

'''
Lógica:
- Pegar a string original.
- Criar um dicionário vazio para armazenar os resultados.
- Verificar cada caractere da string, um por um:
    - Se o caractere já está no dicionário, aumente sua contagem em +1.
    - Se o caractere não está no dicionário, adicione-o com valor inicial 1.
- Resultado final: Um dicionário onde cada chave é um caractere único, e o valor é quantas vezes ele aparece.
'''
string = input('Digite um texto: ')
dicionario_string = {}
 
for caractere in string: 
    if caractere in dicionario_string: 
        dicionario_string[caractere] += 1
    else:
        dicionario_string[caractere] = 1
    
print(dicionario_string)