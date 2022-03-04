print('{:=^40}'.format(' CALCULADORA DE PA 2.0 '))
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
count = 10
total = 0

while count != 0:
    total += count
    while count > 0:
        print(primeiro, end=' ')
        primeiro += razao
        count -= 1
    count = int(input('\nQuantos termos mais gostaria de saber? '))
print('Você visualizou {} termos'.format(total))
print('FIM DO PROGRAMA')

