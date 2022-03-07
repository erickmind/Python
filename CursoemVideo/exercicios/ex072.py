num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    val = -1
    while val not in range(0, 21):
        val = int(input('Digite um número entre 0 e 20: '))
    print(f'O número digitado foi {num[val]}')
    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ').strip().upper()
    if opcao in 'N':
        break

