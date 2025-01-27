'''Analisador'''
maioridade = 0
media = 0
mm20 = 0
for c in range(1, 5):
    print('---- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: ')).title().strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    media += idade
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        maioridadenome = nome
    if sexo == 'F' and idade < 20:
        mm20 += 1
print('----- RESULTADOS -----')
print('Média de idade do grupo {:.2f} anos.'.format(media/4))
print('Nome do homem mais velho {}, idade {} anos.'.format(maioridadenome, maioridade))
print('Quantidade de mulheres menores de 20 anos = {}.'.format(mm20))