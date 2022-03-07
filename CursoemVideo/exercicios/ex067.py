print('{:=^40}'.format(' TABUADA v3.0 '))

while True:
        val = int(input('Digite um valor: '))
        if val < 0:
            break
        count = 1
        print('-' * 40)
        while count <= 10:
            print(f'{val} x {count} = {val*count}')
            count += 1
        print('-'*40)
print('FIM DO PROGRAMA')

