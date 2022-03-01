val = int(input('Digite o valor do salário: '))
if val > 1250:
    print('O salário final com aumento será R${:.2f}'.format(val*1.1))
else:
    print('O salário final com aumento será R${:.2f}'.format(val*1.15))
