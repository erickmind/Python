print('{:=^40}'.format(' Lojinha do Serjão '))

total = 0
carosCount = 0
nome = str(input('Digite o nome do produto: '))
preco = float(input('Digite o preço do produto: '))
menorProd = nome
menorPreco = preco
while True:
    opcao = ' '
    if preco > 0:
        total += preco
        if preco < menorPreco:
            menorProd = nome
        if preco > 1000:
            carosCount += 1
    else:
        print('\033[33mAqui não tem produto de graça!\033[m \033[31m>=(\033[m')
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
    print('-' * 50)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
print('='*50)
print(f'O total gasto na compra foi R${total:.2f}')
print(f'O número de produtos acima de R$1000.00 foi {carosCount}')
print(f'O produto comprado mais barato foi \033[34m{menorProd}\033[m que custa \033[34mR${menorPreco:.2f}\033[m')
