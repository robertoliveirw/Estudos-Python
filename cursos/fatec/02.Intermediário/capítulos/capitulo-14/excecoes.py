''' 
- Tratamento de exceção – é o que consideramos no nosso programa quando existe a possibilidade de ocorrência de erros em um trecho de código e que precisamos tratar para que o nosso programa não tenha sua execução interrompida. Este aspecto foi tratado no capítulo 6 do módulo básico;
- Levantamento de exceção – é o que precisamos implementar quando estamos escrevendo um código, uma situação de erro pode ocorrer e queremos gerar uma exceção para ser tratada em outro ponto do programa. Este é o assunto deste capítulo.
'''
def Primo(V):
    '''V deve ser um inteiro maior ou igual a 2.
    Se V for primo retorna True, senão retorna False'''
    
    if type(V) != int:
        raise TypeError('Tipo incorreto. V deve ser <int>')
    if V < 2:
        raise ValueError('Valor inválido. V deve ser maior que 1')

    if V == 2:  # V é 2, portanto é primo
        return True
    elif V % 2 == 0:  # V é par maior que 2, portanto não é primo
        return False
    else:  # testa se V ímpar é primo
        raiz = int(pow(V, 0.5))  # Convertendo para inteiro para evitar problemas
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False  # se for divisível retorna falso imediatamente
            i += 2
        return True  # se chegar no final do laço então é primo
