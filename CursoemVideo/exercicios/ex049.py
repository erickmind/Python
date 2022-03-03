print('{:=^40}'.format(' TABUADA DO SERJÃO '))
val = int(input('Digite um valor: '))
print('A tabuada de {} é:'.format(val))
for i in range(1, 11):
    print('{} x {}: {}'.format(i, val, val*i))
