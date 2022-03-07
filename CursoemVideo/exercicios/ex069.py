print('{:=^40}'.format(' Análise de dados de um grupo '))
maiores = 0
homens = 0
mulheresMenores = 0

while True:
    cont = ' '
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F':
        if idade < 20:
            mulheresMenores += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
    print('-'*50)
print('='*50)
print(f'O número de pessoas com mais de 18 anos é {maiores}')
print(f'O número de homens no grupo é {homens}')
print(f'O número de mulheres abaixo de 20 anos é {mulheresMenores}')
