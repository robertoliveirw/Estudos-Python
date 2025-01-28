'''ler um número inteiro e mostrar os n primeiros elementos de uma sequencia de fibonacci'''

n = int(input("Digite quantos elementos da sequência de Fibonacci você deseja: "))

a, b = 0, 1
contador = 0

# Verifica se o número é válido
if n <= 0:
    print("Por favor, digite um número maior que 0.")
elif n == 1:
    print(f"Sequência de Fibonacci com {n} elemento:")
    print(a)
else:
    print(f"Sequência de Fibonacci com {n} elementos:")
    while contador < n:
        print(a, end=" ")  # Exibe o valor atual de a
        proximo = a + b  # Calcula o próximo valor da sequência
        a = b  # Atualiza o valor de a
        b = proximo  # Atualiza o valor de b
        contador += 1 
