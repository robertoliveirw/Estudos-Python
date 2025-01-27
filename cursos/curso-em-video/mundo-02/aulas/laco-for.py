# Uso do laço For:
for c in range (0,10):
    print('Hello, World!')
print('End')

# Uso do laço For com aliteração:
for c in range (0,10,2): # O terceiro termo dentro do range é a aliteração
    print(c)
print('End')

for c in range (10,0,-1): # O terceiro termo dentro do range é a aliteração
    print(c)
print('End')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range (i,f+1,p): # O terceiro termo dentro do range é a aliteração
    print(c)
print('End')