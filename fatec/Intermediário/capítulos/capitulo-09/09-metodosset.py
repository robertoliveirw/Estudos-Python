# Operações com conjuntos em Python

# 1. .add()
conjunto = {1, 2, 3}
conjunto.add(4)
print(f"Após add(4): {conjunto}")

# 2. .clear()
conjunto.clear()
print(f"Após clear(): {conjunto}")

# 3. .copy()
conjunto = {1, 2, 3}
copia = conjunto.copy()
print(f"Cópia do conjunto: {copia}")

# 4. .difference()
conj1 = {1, 2, 3}
conj2 = {3, 4, 5}
print(f"Difference: {conj1.difference(conj2)}")

# 5. .difference_update()
conj1.difference_update(conj2)
print(f"Após difference_update: {conj1}")

# 6. .discard()
conjunto = {1, 2, 3}
conjunto.discard(2)
print(f"Após discard(2): {conjunto}")

# 7. .intersection()
conj1 = {1, 2, 3}
conj2 = {2, 3, 4}
print(f"Intersection: {conj1.intersection(conj2)}")

# 8. .intersection_update()
conj1.intersection_update(conj2)
print(f"Após intersection_update: {conj1}")

# 9. .isdisjoint()
conj1 = {1, 2}
conj2 = {3, 4}
print(f"Is disjoint: {conj1.isdisjoint(conj2)}")

# 10. .issubset()
conj1 = {1, 2}
conj2 = {1, 2, 3}
print(f"Is subset: {conj1.issubset(conj2)}")

# 11. .issuperset()
print(f"Is superset: {conj2.issuperset(conj1)}")

# 12. .pop()
conjunto = {1, 2, 3}
elemento_removido = conjunto.pop()
print(f"Elemento removido com pop(): {elemento_removido}, Conjunto restante: {conjunto}")

# 13. .remove()
conjunto = {1, 2, 3}
conjunto.remove(2)
print(f"Após remove(2): {conjunto}")

# 14. .symmetric_difference()
conj1 = {1, 2, 3}
conj2 = {3, 4, 5}
print(f"Symmetric difference: {conj1.symmetric_difference(conj2)}")

# 15. .symmetric_difference_update()
conj1.symmetric_difference_update(conj2)
print(f"Após symmetric_difference_update: {conj1}")

# 16. .union()
conj1 = {1, 2}
conj2 = {3, 4}
print(f"Union: {conj1.union(conj2)}")

# 17. .update()
conj1.update(conj2)
print(f"Após update: {conj1}")
