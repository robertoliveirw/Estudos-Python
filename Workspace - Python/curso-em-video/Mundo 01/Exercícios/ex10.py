# Obter taxa do dolar

dolar = float(input('Digite a taxa do dolar: '))

real = float(input("Digite o valor em reais (R$): "))

valor_dolar_para_real = real / dolar

print(f"R$ {real:.2f} equivalem a $ {valor_dolar_para_real:.2f}")
