s=123

for d in str(s):
    match d:
        case 3: print('x', end='')
        case 2: print('a', end='')
        case 1: print('y', end='')
        case _: print('z', end='')
    