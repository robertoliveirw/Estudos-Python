'''Empréstimo Bancário
Valor da Casa OK
Salário OK
Quantos anos vai pagar OK

Pretação mensal não pode exceder 30% do salário ou então o empréstimo será negado'''
print('Calculadora de Financiamento')

vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
mensalidade = (vcasa/anos)/12
prestacao = salario*0.3

if prestacao <= mensalidade:
    print('Financiamento Rejeitado!')
else:
    print('Aprovado')