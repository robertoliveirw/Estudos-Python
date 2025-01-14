# Maior aparição lista de frequencia


votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

contagem_votos = {}

for produtos in votos:
    if produtos in contagem_votos:
        contagem_votos[produtos] += 1
    else:
        contagem_votos[produtos] = 1

print(contagem_votos)
