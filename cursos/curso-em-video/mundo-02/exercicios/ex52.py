'''Ler se o número é primo ou não'''
n = int(input('verificar primos até: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        tot += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso é primo.')
else:
    print('Por isso não é primo.')