# Exemplo 12.19
'''Função  map - A função map() aplica a funçãoao iterável passado. Caso a funçãotenha mais de um argumento outros iteráveis devem ser passados. '''

dados = [2, 3, 4, 5, 6]
a  = list(map(lambda x: x * 10, dados))

print(a)
