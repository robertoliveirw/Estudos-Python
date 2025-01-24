# Exemplo 12.7
'''Parametro com valor padrão'''

# Função Criada
def saudacao(nome, mensagem = 'Olá'):
    print(mensagem, nome)

# Código Principal
saudacao = ('Roberto', 'Boa tarde')
print(saudacao)

saudacao = ('Roberto')
print(saudacao)