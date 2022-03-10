from datetime import date
nome = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
cart = int(input('Digite a Carteira de Trabalho (0 não tem): '))
nasc = date.today().year - ano

pessoa = {}
pessoa['nome'] = nome
pessoa['idade'] = nasc
pessoa['carteira'] = cart

if cart != 0:
    contrato = int(input('Digite o ano de contratação: '))
    salario = float(input('Digite o seu salário: '))
    pessoa['contrato'] = contrato
    pessoa['salario'] = salario

print(f'O nome é {pessoa["nome"]}')
print(f'A idade é {pessoa["idade"]}')
print(f'O CTPS é {pessoa["carteira"]}')
if cart != 0:
    print(f'O ano de contratação é {pessoa["contrato"]}')
    print(f'O salario é {pessoa["salario"]}')

print(f'{pessoa["nome"]} irá se aposentar com {pessoa["idade"] + 35 - (date.today().year - pessoa["contrato"])} anos')

