import random

tupla = (random.random(), random.random(), random.random(), random.random(), random.random())

print(f'A tupla gerada foi {tupla}')

#print(f'O menor valor da tupla é {sorted(tupla)[0]}')
print(f'O menor valor da tupla é {min(tupla)}')

#print(f'O maior valor da tupla é {sorted(tupla)[-1]}')
print(f'O menor valor da tupla é {max(tupla)}')
