l1 = float(input('Digite o valor da primeira reta: '))
l2 = float(input('Digite o valor da segunda reta: '))
l3 = float(input('Digite o valor da terceira reta: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
