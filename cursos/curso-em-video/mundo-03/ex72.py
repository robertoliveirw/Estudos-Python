'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
'''

tupla = (
    'Zero', 
    'Um', 
    'Dois', 
    'Três', 
    'Quatro', 
    'Cinco', 
    'Seis', 
    'Sete', 
    'Oito', 
    'Nove', 
    'Dez', 
    'Onze', 
    'Doze', 
    'Treze', 
    'Quatorze', 
    'Quinze', 
    'Dezesseis', 
    'Dezessete', 
    'Dezoito', 
    'Dezenove', 
    'Vinte'
)


while True:
    numero = int(input('Digite um número:'))
    
    if numero < 0 or numero > 20:
        continue
    
    print(f'O número por extenso é: {tupla[numero]}')
    break
