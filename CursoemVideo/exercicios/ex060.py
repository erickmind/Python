print('{:=^40}'.format(' CALCULADORA DE FATORIAL '))
val = int(input('Digite um valor: '))
c = val
fatorial = 1

print('{}!'.format(val), end=' = ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)
