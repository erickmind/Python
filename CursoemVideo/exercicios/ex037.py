import math
val = int(input('Digite um valor inteiro: '))
print('Qual será a base de conversão?\n1 para binário\n2 para octal\n3 para hexadecimal')
base = int(input('Sua opção: '))

if base == 1:
    print('O valor em binário será: {}'.format(bin(val)[2:]))
elif base == 2:
    print('O valor em octal será: {}'.format(oct(val)[2:]))
elif base == 3:
    print('O valor em hexadecimal será: {}'.format(hex(val)[2:]))
else:
    print('\033[31mOpção inválida de base de conversão!\033[m')
