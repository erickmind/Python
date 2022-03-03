val = int(input('Digite um valor: '))
flag = False
for i in range(2, val):
    if val % i == 0:
        flag = True
if flag == True:
    print('O valor NÃO é um número primo')
else:
    print('O valor é um número primo')

