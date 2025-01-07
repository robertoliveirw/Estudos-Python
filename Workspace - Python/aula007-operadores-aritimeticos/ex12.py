# Entrada de dados
preco = float(input("Digite o preço de um produto: \nR$"))


desconto = preco * 5 / 100

print(f"Na liquidação da loja, esse produto de R${
      preco:.2f} está com desconto de 5%, \n ou seja, vai custar só R${preco - desconto:.2f}.")
