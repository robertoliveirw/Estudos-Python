# Exercício de Mach-case

produto = -1

print('Leitor de produtos! \n \n')

while produto != 0:
    
    produto = int(input('Qual o código do produto que você quer verificar? \n digite \'0\' para finalizar.'))

    match produto:
        case 16: 
            print('Bebê')
        case 23: 
            print('Infantil Feminino')
        case 25: 
            print('Infantil masculino')
        case 29: 
            print('Infantil esportivo')
        case 42: 
            print('Masculino Formal')
        case 43: 
            print('Masculino Casual')
        case 49: 
            print('Masculino Esportivo')
        case 52: 
            print('Femino Formal Salto Baixo')
        case 53: 
            print('Femino Formal Salto Alto')
        case 55: 
            print('Feminino casual salto baixo')
        case 56: 
            print('Feminino Casual salto alto')
        case 59: 
            print('Feminino esportivo')
        case 0:
            print(' \n Programa Finalizado')
        case _ :
            print('Inválido')
    


    