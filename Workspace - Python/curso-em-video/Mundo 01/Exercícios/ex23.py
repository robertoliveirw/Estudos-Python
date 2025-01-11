# Ler os números de 0 a 9999 e mostra na tela cada um dos dígitos separados (Unidade, dezena, centena, milhar)

numero = int(input('Digite um número entre 0 e 9999: \n'))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"Numero: {numero} | 23: {milhar} | Centena: {
      centena} | Dezena: {dezena} | Unidade: {unidade}")
