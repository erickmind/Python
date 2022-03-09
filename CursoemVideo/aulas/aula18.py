teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

turma = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(turma[2][1])
for p in turma:
    print(f'{p[0]} tem {p[1]} anos')

grupo = list()
dado = list()
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()

maior = 0
menor = 0
for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor += 1

print(f'Temos {maior} maiores de idade e {menor} menores')


