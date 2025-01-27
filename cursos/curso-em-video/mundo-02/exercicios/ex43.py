'''IMC'''

# Calculadora de IMC
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o IMC com classificação
print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc <= 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= imc <= 34.9:
    print("Classificação: Obesidade grau 1")
elif 35 <= imc <= 39.9:
    print("Classificação: Obesidade grau 2")
else:  # IMC >= 40
    print("Classificação: Obesidade grau 3 ou mórbida")
