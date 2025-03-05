# Gere a sequência de Fibonacci até um número ou quantidade de termos especificada pelo usuário.

print (" Trabalho de Fibonacci ")

n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1

print(f"{t1} . {t2} .",end="")

cont = 6

while cont <= n:
    t3 = t1 + t2
    print (f"  {t3}.",end="")
    t1 = t2
    t2 = t3
    cont +=1

print( " Fim ")  