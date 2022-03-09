linha = []
matriz = [linha[:], linha[:], linha[:]]

for posLinha, i in enumerate(matriz):
    for j in range(0, 3):
        val = int(input(f'Digite o valor da posição [{posLinha}, {j}] da matriz: '))
        matriz[posLinha].append(val)

for pos, i in enumerate(matriz):
    for j in matriz[pos]:
        print(f'[{j:^5}]', end='')
    print('')

pares = 0
terceira = 0
maiorSegunda = matriz[0][0]

for posLinha, linha in enumerate(matriz):
    for posCol, coluna in enumerate(matriz[posLinha]):
        if coluna % 2 == 0:
            pares += coluna
        if posCol == 2:
            terceira += coluna
        if posLinha == 1:
            if coluna > maiorSegunda:
                maiorSegunda = coluna

print(f'A soma de todos os valores pares da matriz é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maiorSegunda}')




