# ler um angulo qualquer mostrar o seno, cosseno e tangente

import math

ang = float(input('Digite o angulo: '))
rad = math.radians(ang)  # tranformando de angulo para radiano

seno = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)

print(f'O seno é {seno}, o cosseno é {cos} e a tangente é {tg}')