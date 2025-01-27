'''Criar um pedra papel e tesoura'''

import random

jokenpo = random.randint(0, 2)

if jokenpo == 0:
    jokenpo = 'Pedra'
elif jokenpo == 1:
    jokenpo = 'Papel'
else:
    jokenpo = 'Tesoura'

usuario_escolha = int(input('O que você deseja: Pedra(1), Papel(2) ou Tesoura(3)?'))

# Escolha do usuário: Pedra
if usuario_escolha == 1 and jokenpo == 'Pedra':
    print(f'O computador escolheu {jokenpo}. Empate!')
elif usuario_escolha == 1 and jokenpo == 'Papel':
    print(f'O computador escolheu {jokenpo}. Derrota!')
elif usuario_escolha == 1 and jokenpo == 'Tesoura':
    print(f'O computador escolheu {jokenpo}. Vitória!')
# Escolha do usuário: Papel
elif usuario_escolha == 2 and jokenpo == 'Pedra':
    print(f'O computador escolheu {jokenpo}. Vitória!')
elif usuario_escolha == 2 and jokenpo == 'Papel':
    print(f'O computador escolheu {jokenpo}. Empate!')
elif usuario_escolha == 2 and jokenpo == 'Tesoura':
    print(f'O computador escolheu {jokenpo}. Derrota!')
# Escolha do usuário: Tesoura
elif usuario_escolha == 3 and jokenpo == 'Pedra':
    print(f'O computador escolheu {jokenpo}. Derrota!')
elif usuario_escolha == 3 and jokenpo == 'Papel':
    print(f'O computador escolheu {jokenpo}. Vitória!')
elif usuario_escolha == 3 and jokenpo == 'Tesoura':
    print(f'O computador escolheu {jokenpo}. Empate!')