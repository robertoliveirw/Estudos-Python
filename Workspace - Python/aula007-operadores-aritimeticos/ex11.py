# Entrada de dados
largura = float(input("Digite a largura (m): "))
altura = float(input("Digite a altura (m): "))

area = largura * altura

print(f"Sua parede tem a dimensão {largura}x{
      altura} e sua área é de {area:.2f} m².")

tinta_necessaria = area / 2
print(f"Para pintar essa parede, você precisará de {
      tinta_necessaria:.2f} litros de tinta.")
