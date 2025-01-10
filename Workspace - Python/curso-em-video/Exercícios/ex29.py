# ler a velocidade de um carro e aplicar uma multa caso esteja acima de 80km/h de 7 reais por km acima

import random

velocidade = random.randint(0, 120)

print(f'Você passou a: {velocidade}Km/h')

if velocidade <= 80:
    print('Dentro do limite de velocidade')
else:
    kmamais = velocidade - 80
    multa = kmamais * 7
    print(f'Você passou a {velocidade}Km/h, sendo isso {
          kmamais}Km/h acima do limite permitido. Sua multa é de {multa}')
