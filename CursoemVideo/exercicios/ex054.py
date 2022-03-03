from datetime import date

soma = 0
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(i)))
    idade = date.today().year - ano
    if idade >= 18:
        print('Essa pessoa já atingiu a maioridade!')
        soma += 1
print('{} pessoas já atingiram a maioridade!'.format(soma))
print('{} pessoas ainda são menores de idade!'.format(7 - soma))
