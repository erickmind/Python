lista = []

while True:
    val = int(input('Digite um valor: '))
    lista.append(val)
    opcao = ' '
    while opcao not in 'S/N':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

pares = []
impares = []
for elem in lista:
    if elem % 2 == 0:
        pares.append(elem)
    else:
        impares.append(elem)

print(f'Lista inteira {lista}')
print(f'Lista de pares {pares}')
print(f'Lista de ímpares {impares}')
