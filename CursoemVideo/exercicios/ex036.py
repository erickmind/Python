casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário do comprador: '))
anos = float(input('Em quantos anos o comprador irá pagar a casa? '))

meses = anos * 12
if (casa/meses) <= (salario*0.3):
    print('A prestação mensal será de: R${:.2f}'.format(casa/meses))
else:
    print('A prestação excede 30% do salário do comprador. \033[31mEmpréstimo negado!\033[m')
