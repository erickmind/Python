val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if val1 > val2:
    print('O primeiro valor {} é maior do que o segundo {}'.format(val1, val2))
elif val2 > val1:
    print('O segundo valor {} é maior do que o primeiro {}'.format(val2, val1))
else:
    print('Os valores digitados são iguais!')
