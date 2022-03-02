from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
alist = 18 - idade
if idade < 18:
    print('Ainda não é hora de se alistar no exército! Seu alistamento será em {}'.format(date.today().year + alist))
    print('Faltam {} anos para você poder se alistar!'.format(alist))
elif idade == 18:
    print('\033[33mEsse ano você deve se alistar!\033[m')
else:
    alist = idade - 18
    print('\033[31mVocê já passou do tempo de se alistar! Seu alistamento foi em {}\033[m'.format(date.today().year - alist))
    print('\033[31mJá se passaram {} anos do prazo de alistamento!\033[m'.format(alist))
