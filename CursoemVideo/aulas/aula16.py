lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata')

print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-3:])

# Tuplas são imutáveis!
#lanche[1] = 'Refrigerante'

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Na geladeira tem: {comida}, na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
c = b + a
print(c)
print(c.count(5))
print(c.index(5))
print(c.index(5, 1))

teste = (1, 2)
del(teste)
#print(teste)
