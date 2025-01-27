'''Calculadora de meédia:
Abaixo de 5 reprovado
Entre 5 e 6.9 recuperação
Acima de 7 aprovado'''


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3


print(f"\nSua média é: {media:.2f}")


if media < 5:
    print("Situação: REPROVADO")
elif 5 <= media <= 6.9:
    print("Situação: RECUPERAÇÃO")
else:  # média >= 7
    print("Situação: APROVADO")
