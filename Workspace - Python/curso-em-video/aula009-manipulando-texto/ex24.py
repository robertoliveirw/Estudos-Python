# Verificar se o nome da cidade começa com Santo

cidade = str(input('Em qual cidade você nasceu? \n')).strip()
print(cidade[0:5].upper() == 'SANTO')
# Com a função Strip() eu estou removendo os espaços indesejados tanto do final quanto do início.
# Com os [] Eu estou delimitando o primeiro caractere (0) e o último caracter da palavra SANTO (5), era para ser 4, mas começa no 0.
# Eu estou usando .upper() para poder testar sempre com tudo maiúsculo e evitar erros.
