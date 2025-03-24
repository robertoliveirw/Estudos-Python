'''
Crie um progrmaa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
Mostre uma lsitagem de preços organizandos os prelos de maneira tabular
'''
tupla_produtos = (
                    'leite', 4,
                    'Amaciante', 15,
                    'Gelo', 2, 
                    'Refrigerante', 12
                  )

tamanho = 30

print('-'*tamanho)
print('Lista de Preços'.center(tamanho))
print('-'*tamanho)

for i in range(0, len(tupla_produtos),2):
    produto = tupla_produtos[i]
    preco = tupla_produtos[i+1]
    pontos = '.' * (tamanho - len(produto) - len(str(preco)))
    print(f'{produto}{pontos}{preco}')
