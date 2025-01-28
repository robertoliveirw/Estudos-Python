'''Ler nome e preço de vários produtos. Perguntar se quer continuar add dados. 

a -Total Gasto na compra - OK
b - Produtos que custam mais de 1000 - OK
c - Produto mais barato (retornar o nome)'''

total_gasto, acima1k, menor_valor, contador = 0, 0, 0, 0 

while True:
    nome_produto = input('Produto: ')
    valor_produto = float(input('Valor do produto: '))
    
    # Soma do total de produtos gastos
    total_gasto += valor_produto

    # Produtos que custam mais de R$ 1000
    if valor_produto > 1000:
        acima1k += 1

    # Produto mais barato
    contador += 1
    if contador == 1:
        menor_valor = valor_produto
        nome_produto_menor_valor = nome_produto
    elif valor_produto < menor_valor:
        menor_valor = valor_produto
        nome_produto_menor_valor = nome_produto

    # Usuário responder se quer ou não continuar
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja adicionar mais produtos? [S/N]').strip().upper()[0]
    if resposta == 'N':
       break

print(f'Total gasto: {total_gasto}')
print(f'São {acima1k} produtos acima de R$ 1000')
print(f'O produto de menor valor é {nome_produto_menor_valor} custando R$ {menor_valor}')
print('Fim do programa')