# ler o o salário de um funcionário. Se for acima de 1250 acrescer 10% se for abaixo, acrescer 15%

salario = float(input('Qual o seu salário? \n'))

if salario > 1250:
    novosal = salario*1.1
    print(f'Seu novo salário é de R$ {novosal:.2f}')
else:
    novosal = salario*1.15
    print(f'Seu novo salário é de R$ {novosal:.2f}')
