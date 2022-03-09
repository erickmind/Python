numeros = [[], []]

for i in range(0, 7):
    val = int(input('Digite um valor: '))
    if val % 2 == 0:
        numeros[0].append(val)
    else:
        numeros[1].append(val)

numeros[0].sort()
numeros[1].sort()

print(f'PARES: {numeros[0]}')
print(f'IMPARES: {numeros[1]}')
