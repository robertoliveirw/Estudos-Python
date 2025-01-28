# Laço While 
c = 0
num = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    c += num


print(c)