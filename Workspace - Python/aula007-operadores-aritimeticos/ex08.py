# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input("Digite um valor em metros: \n"))  # O \n é a quebra de linha


print(f"{n} metros são {n*1000} kilômetros.")
print(f"{n} metros são {n*100} hectômetros.".format(n, n * 100))
print(f"{n} metros são {n*10} decâmetros.".format(n, n * 10))

print(f"{n} metros são {n*1} metros.".format(n, n * 1))

print(f"{n} metros são {n/10} decímetros.".format(n, n / 10))
print(f"{n} metros são {n/100} centímetros.".format(n, n / 100))
print(f"{n} metros são {n/1000} milímetros.".format(n, n / 1000))
