# Programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa

cathet1 = float(input('Digite o valor do cateto adjacente: '))
cathet2 = float(input('Digite o valor do cateto oposto: '))

hypotenuse = cathet1*2 + cathet2*2

print(f'O valor da hipotenusa é {hypotenuse}')
