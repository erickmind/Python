n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2)/2

print('O aluno tirou as notas {:.1f} e {:.1f} e sua média foi {}'.format(n1, n2, media))
if media >= 7:
    print('\033[32mAPROVADO!\033[m')
elif media < 7 and media >= 5:
    print('\033[33mRECUPERAÇÃO!\033[m')
else:
    print('\033[31mREPROVADO!\033[m')
