# Entrada de dados
dias = int(input("Por quantos dias o carro foi alugado: \n"))
km = float(input("Quantos km o carro rodou: \n"))


custo_dias = dias * 60
custo_km = km * 0.15


print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${
      custo_km + custo_dias:.2f}.")

# OK
