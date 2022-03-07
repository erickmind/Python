import time

print('{:=^40}'.format('\033[35m CAIXA ELETRÔNICO \033[m'))

while True:
    opcao = 'A'
    cinquenta = 0
    vinte = 0
    dez = 0
    um = 0
    print('\n\033[33mEstão disponíveis apenas cédulas de R$50, $20, R$10 e R$1!\n\033[m')
    val = int(input('Digite o valor a ser sacado: '))

    unidade = val % 10
    if 0 < unidade < 10:
        um = unidade
        val = val - um
    if val >= 50:
        cinquenta = val // 50
        val = val - cinquenta*50
    if val >= 20:
        vinte = val // 20
        val = val - vinte*20
    if val >= 10:
        dez = val // 10
        val = val - dez*10

    print('='*50)
    print(f'''Serão impressas:
    {cinquenta:.0f} notas de 50
    {vinte:.0f} notas de 20
    {dez:.0f} notas de 10
    {um:.0f} notas de 1\n''')

    print('\033[33mREALIZANDO SAQUE ...\033[m')
    time.sleep(2)
    print('=' * 50)

    while opcao not in 'SN':
        opcao = str(input('Deseja realizar outro saque? [S/N] ')).strip().upper()[0]
    if opcao in 'N':
        break
print('FIM DO PROGRAMA')