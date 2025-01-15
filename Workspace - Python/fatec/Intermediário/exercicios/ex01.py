# Exercício de Mach-case

produto = -1

print('Leitor de produtos! \n \n')

while produto != 0:
    
    produto = int(input('Qual o código do produto que você quer verificar? \n digite \'0\' para finalizar.'))

    match produto:
        Case 16: 
            print('Bebê')
        Case 23: 
            print('Infantil Feminino')
        Case 25: 
            print('Infantil masculino')
        Case 29: 
            print('Infantil esportivo')
        Case 42: 
            print('Masculino Formal')
        Case 43: 
            print('Masculino Casual')
        Case 49: 
            print('Masculino Esportivo')
        Case 52: 
            print('Femino Formal Salto Baixo')
        Case 53: 
            print('Femino Formal Salto Alto')
        Case 55: 
            print('Feminino casual salto baixo')
        Case 56: 
            print('Feminino Casual salto alto')
        Case 59: 
            print('Feminino esportivo')
        case _ :
            print('Inválido')
    
print(' \n Programa Finalizado')

    