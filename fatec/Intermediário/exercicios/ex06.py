''' Escreva um prograsma que leia do teclado o código de um produto e seu preço unitário. O código é uma string e o preço é real. Acrescente o par código: Preço em um dicionário. O programa deve verificar se o cpodigo já está no dicionário e nesete caso deve emitir uma mensagem de erro. O laço termina quando for fornecido um string vazio para o código., Ao final, exibir código e preço, em um produto em cada linha'''

item = {}

print('Início do Programa')

while True:
     
    codigo = input('Digite o código do produto: ')

    if codigo == '':
        print('\n Fim do programa.')
        break
    elif codigo in item:
        print(f'\n o código {codigo} já existe no programa.')
         

    preco = float(input('Digite o preço do produto: '))
    item[codigo] = ((preco))

print(f'\n Esta é a lista de Produtos(codigos) e Preços: {item}')
    
   