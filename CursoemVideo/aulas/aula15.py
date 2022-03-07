n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salario = 900.2
print(f'O {nome:^20} tem {idade:-<20} e ganha R${salario:.2f}')
