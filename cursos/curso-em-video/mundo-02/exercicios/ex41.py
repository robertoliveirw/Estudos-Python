'''Ler a idade do atleta e retornar:
- Até 9 anos: MIirm
Até 14 anos Infantil
até 19 anos Junior
Até 20 anos Senior
Acima Master'''

idade = int(input("Digite a idade do atleta: "))

# Classificação por idade
if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Junior"
elif idade == 20:
    categoria = "Senior"
else:
    categoria = "Master"

print(f"O atleta tem {idade} anos e está na categoria: {categoria}")