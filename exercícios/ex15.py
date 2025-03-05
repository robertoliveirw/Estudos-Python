# Converta uma temperatura de Celsius para Fahrenheit e vice-versa.

temp = float(input('Digite uma temperatura: '))
f_ou_c = int(input('Digite a opçao que deseja converter: \n 1 - Converter para Celsius \n 2 - Converter para Fahrenheit'))

if f_ou_c == 1: 
    temp_convertida_para_fahrenheit = 1.8*temp + 32
    print('A temperatura em Fahrenheit é de: ', temp_convertida_para_fahrenheit)
else:
    temp_convertida_para_celsius = (temp-32)/1.8
    print('A temperatura em Celsis é de: ', temp_convertida_para_celsius)