'''Exercício Resolvido 12.8
Escreva um programa que utilize uma função recursiva para realizar uma contagem regressiva. Este programa deve ler do teclado um inteiro que representa a quantidade de toques dessa contagem regressiva. Quando a contagem chegar em zero o programa deve exibir na tela a mensagem "NO AR!!!" '''

def Contagem(cont):
    if cont == 0:
        print("NO AR!!!")
    else:   
        print(cont)
        Contagem(cont-1)

toques = int(input('Digite a quantidade de toques da contagem: '))
print(f'Atenção para o toque de {toques} segundos...')
print(f'Atenção para o toque de {toques} segundos...')
print(Contagem(toques))