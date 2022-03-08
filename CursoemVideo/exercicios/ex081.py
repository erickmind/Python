lista = []
count = 0
hasFive = False

while True:
    opcao = ' '
    val = int(input('Digite um valor: '))
    lista.append(val)
    count += 1
    if 5 in lista:
        hasFive = True
    while opcao not in 'S/N':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opcao in 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {count} números')
print(f'A lista de valores em ordem decrescente é {lista}')
if hasFive:
    print('\033[32mO 5 foi digitado e está na lista\033[m')
else:
    print('\033[31mO 5 não foi digitado e não está na lista\033[m')