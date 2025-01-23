# Exemplo 12.4


# Função Criada
def geradados():
    """Esta função inicializa 7 objetos de diferentes classes e os retorna"""
    a = 16
    b = 39.7
    c = 'texto'
    d = [1, 2, 3, 4]
    e = (0, 1)
    f = {80, 90, 100}
    g = frozenset((3, 4, 5))
    return a, b, c, d, e, f, g # Este retorno equivale a uma tupla. É o mesmo que (a, b, c, d, e, f, g)
    

# Código Principal
dados = geradados()
for x in dados:
    print(f' {x} é objeto da classe {type(x)}')
