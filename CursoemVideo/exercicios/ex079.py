lista = []

while True:
    opcao = ' '
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
    else:
        print('Valor duplicado! Não vou adicionar.')
    while opcao not in 'S/N':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao in 'N':
        break

lista.sort()
print(lista)
