print('{:=^40}'.format(' CALCULADORA DE PA '))
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
cont = 10

while cont > 0:
    print(primeiro, end=' ')
    primeiro += razao
    cont -= 1
