'''Condição de Pagamento
A vista (Dinheiro): 10% de desconto
A vista (Cartão): 5% de desconto
2x no cartão preço normal
3x ou mais no cartão 20% de juros
'''
preco = float(input('Qual o valor do produto? '))
prazo_ou_a_vista = int(input('Você deseja pagar a vista (1) ou a prazo (2)? '))

if prazo_ou_a_vista == 1:
    dinheiro_ou_cartao = int(input('Você deseja pagar no dinheiro(1) ou no cartão (2)? '))
    if dinheiro_ou_cartao == 1:
            nvalor = preco*0.90
            print(f'Você vai pagar em dinheiro, por esse motivo, tem um desconto de 10%, novo valor de: R${nvalor:.2f}')
    else:
            nvalor = preco*0.95
            print(f'Você vai pagar no cartão, por esse motivo, tem um desconto de 5%, novo valor de: R${nvalor:.2f}')
else:
    vezes_a_pagar = int(input('Você deseja pagar em 2 vezes(1) ou mais de 2(2)? '))
    if vezes_a_pagar == 1:
        print('Sem desconto!')
    else:
        nvalor = preco*1.20
        print(f'Você vai pagar no cartão em 3x ou mais, por esse motivo, tem um acréscimo de 20%. Novo valor de: R${nvalor:.2f}')