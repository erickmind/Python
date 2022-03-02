print('{:=^40}'.format(' CROAK STORE '))
prod = float(input('Digite o preço do produto: '))

print('\033[33mEscolha uma opção de pagamento: \033[m')
print('\033[35m1:\033[m À vista\n\033[35m2:\033[m À vista no cartão\n'
      '\033[35m3:\033[m Em 2x no cartão\n\033[35m4:\033[m 3x ou mais no cartão')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print('O preço a pagar será: R${:.2f} à vista'.format(prod*0.9))
elif opcao == 2:
    print('O preço a pagar será: R${:.2f} à vista no cartão'.format(prod*0.95))
elif opcao == 3:
    print('O preço a pagar será: R${:.2f} em 2 parcelas de R${:.2f}'.format(prod, prod/2))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    print('O preço a pagar será: R${:.2f} em {} parcelas de R${:.2f}'.format(prod*1.2, parcelas, (prod*1.2)/parcelas))
else:
    print('\033[31mOpção Inválida!\033[m')