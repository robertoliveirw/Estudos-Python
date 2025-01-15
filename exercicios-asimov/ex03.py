# Quem gastou mais dinheiro?

gastos_lucas = [200, 300, 500, 600]
gastos_marcos = [50, 60, 140, 200, 700]

total_gastos_lucas = sum(gastos_lucas)
total_gastos_marcos = sum(gastos_marcos)

if total_gastos_lucas > total_gastos_marcos:
    diferenca = total_gastos_lucas - total_gastos_marcos
    print(f'Lucas gastou mais dinheiro do que Marcos! \n  Lucas gastou R$ {
          diferenca} a mais que Marcos. Totalizando: R$ {total_gastos_lucas}')
elif total_gastos_marcos > total_gastos_lucas:
    diferenca = total_gastos_marcos - total_gastos_lucas
    print(f'Marcos gastou mais dinheiro do que Lucas! \n  Marcos gastou R$ {
          diferenca} a mais que Lucas. Totalizando: R$ {total_gastos_marcos}')
else:
    print(f'Eles gastaram a mesma quantidade: R$ {gastos_lucas}')
