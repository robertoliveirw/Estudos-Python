# PH da água

ph = float(input('Digite o PH da água: '))

if ph < 6:
    print('Solução Ácida')
elif ph >= 6 and ph < 7:
    print('Solução levemente ácida')
elif ph == 7:
    print('Solução Neutra')
elif ph > 7 and ph < 8:
    print('Soluão Levemente Alcalina')
else:
    print('Alcalina')
