lista = []

for i in range(0, 5):
    val = int(input(f'Digite um valor para a posição {i}: '))
    lista.append(val)
    if i == 0:
        maior = menor = val
    else:
        if val > maior:
            maior = val
        if val < menor:
            menor = val

print(f'O maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=' ')
print(f'\nO menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=' ')
