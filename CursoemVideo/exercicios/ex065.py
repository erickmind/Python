print('{:=^40}'.format(' CALCULADORA DE MÉDIA '))

val = float(input('Digite um valor: '))
soma = val
n = 1
maior = val
menor = val

opcao = 'S'
while opcao == 'S':
    val = float(input('Digite mais um valor: '))
    if val > maior:
        maior = val
    if val < menor:
        menor = val
    soma += val
    n += 1
    opcao = str(input('Deseja continuar? [S/N] '))
    media = soma/n

print('A média dos valores é: {:.2f}'.format(media))
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))
print('FIM DO PROGRAMA')
