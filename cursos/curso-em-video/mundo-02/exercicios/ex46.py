'''Contagem regressiva de 10 a 0 com 1 segundo entre elas'''
from time import sleep

for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('FIM')