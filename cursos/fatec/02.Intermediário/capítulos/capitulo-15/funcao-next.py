def gera_simples():
 print(' ...próximo valor retornado = 38')
 yield 38
 print(' ...próximo valor retornado = 159')
 yield 159
 print(' ...próximo valor retornado = 47')
 yield 47
 print(' ...próximo valor retornado = 26')
 yield 26

gerador = gera_simples()

next(gerador)
next(gerador)
next(gerador)
next(gerador)
