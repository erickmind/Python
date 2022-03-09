matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for posLinha, i in enumerate(matriz):
    for j in range(0, 3):
        matriz[posLinha][j] = int(input(f'Digite o valor da posição [{posLinha}, {j}] da matriz: '))

for pos, i in enumerate(matriz):
    for j in matriz[pos]:
        print(f'[ {j:^5} ]', end='')
    print()

