val = soma = count = 0

while val != 999:
    soma += val
    count += 1
    val = int(input('Digite um valor \033[33m(999 para parar o programa)\033[m: '))
print('Foram digitados {} números!'.format(count))
print('A soma entre eles é {}'.format(soma))
