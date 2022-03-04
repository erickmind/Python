val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''    [1] Somar valores
    [2] Multiplicar valores
    [3] Informar qual é o maior
    [4] Digitar novos números
    [5] Sair do programa
    ''')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print('A soma entre os valores {} e {} é {}'.format(val1, val2, val1+val2))
    if opcao == 2:
        print('A multiplicação entre os valores {} e {} é {}'.format(val1, val2, val1*val2))
    if opcao == 3:
        if val1 > val2:
            print('O valor {} é maior que o valor {}'.format(val1, val2))
        elif val2 > val1:
            print('O valor {} é maior que o valor {}'.format(val2, val1))
        else:
            print('Os valores são iguais!')
    if opcao == 4:
        val1 = int(input('Digite o primeiro valor: '))
        val2 = int(input('Digite o segundo valor: '))
print('FIM DO PROGRAMA')
