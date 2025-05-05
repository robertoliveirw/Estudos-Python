def paridade(pvalor): 

    # criando o tratamento de exceção
    if type(pvalor) != int:
        raise Exception('A função deve receber um valor INTEIRO')
    # //

    if pvalor % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
