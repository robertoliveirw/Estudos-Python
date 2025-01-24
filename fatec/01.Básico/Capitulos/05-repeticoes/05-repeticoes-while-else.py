# Para o Programa ao Digitar um número negativo (Com else) ou parar ao digitar 0 (com break)

i = 1

while i > 0:
    i = int(input('Digite um número: \n'))
    if i == 0:
        print('   Você digitou Zero...  \n Programa finalizado  ')
        break
else:
    print('Você digitou um número negativo... \n Programa finalizado')
