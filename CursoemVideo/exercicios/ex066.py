soma = 0
while True:
    val = int(input('Digite um valor \033[33m(999 para parar)\033[m: '))
    if val == 999:
        break
    soma += val
print(f'A soma é {soma}')
