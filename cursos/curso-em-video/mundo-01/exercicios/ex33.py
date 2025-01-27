# ler o3 números e ver qual é o menor e qual o maior?

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))


menor = min(n1, n2, n3)
maior = max(n1, n2, n3)


print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
