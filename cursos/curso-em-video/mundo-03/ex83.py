expr = str(input('Digite a experssão: '))

expr_abre_parenteses = expr.count('(')
expr_fecha_parenteses = expr.count(')')

print('='*30)
if expr_abre_parenteses == expr_fecha_parenteses:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')