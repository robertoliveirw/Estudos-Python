''' 
return → Retorna um valor único e encerra a função.
yield → Retorna múltiplos valores ao longo do tempo, pausando e retomando a execução.

'''
# Exemplo de Return - Função comum:
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Saída: 7

# Exemplo de Yield - Função Geradora:
def contador():
    for i in range(3):
        yield i  # Pausa e retorna i

gen = contador()  # Criando um gerador

for num in gen:  # Iterando sobre o gerador com for
    print(num)
