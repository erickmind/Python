print('{:=^40}'.format(' SEQUÊNCIA DE FIBONACCI '))

n = int(input('Digite um valor: '))
n -= 2
val1 = 0
val2 = 1
print('Os {} primeiros termos da sequência de fibonacci são:'.format(n))
print('{} {}'.format(val1, val2), end=' ')
while n > 0:
    fibo = val1 + val2
    print('{}'.format(fibo), end=' ')
    val1 = val2
    val2 = fibo
    n -= 1
print('\nFIM DO PROGRAMA')