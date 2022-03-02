from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 0:
    print('\033[31mAno de nascimento inválido!\033[m')
elif idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 25:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
