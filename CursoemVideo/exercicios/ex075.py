tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro valor 3 apareceu na posição {tupla.index(3)}')
else:
    print('\033[31mO valor 3 não está na tupla\033[m')

print('Os valores pares são: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
