# Perguntar a distância da viagem e calcular o preço da passagem cobrando 0,50 por km para viagens até 200km e 0,45 para viagens acima de 200km

km = int(input('Qual a distância da viagem?: \n'))

if km <= 200:
    valor = km*0.50
    print(f'O valor da passagem é: R$ {valor:.2f} ')
else:
    valor = km*0.45
    print(f'O valor da passagem é: R$ {valor:.2f} ')
1
