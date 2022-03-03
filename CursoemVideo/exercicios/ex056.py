idadeTotal = 0
menor = 0
maisVelho = None
maior = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {} pessoa: '.format(i)))
    idade = int(input('Digite a idade desta pessoa: '))
    idadeTotal += idade
    print('''Qual é o sexo dessa pessoa?
    \033[35m1:\033[m Masculino
    \033[35m2:\033[m Feminino''')
    sexo = int(input('Digite a opção: '))
    if sexo == 1 and i == 1:
        maior = idade
        maisVelho = nome
    if sexo == 1 and idade > maior:
        maior = idade
        maisVelho = nome
    elif sexo == 2 and idade < 20:
        menor += 1

media = idadeTotal/4
print('A média de idade do grupo é: {}'.format(media))
if maisVelho != None:
    print('O nome do homem mais velho é: {}'.format(maisVelho))
else:
    print('Não há homens no grupo!')
print('{} mulheres no grupo têm menos de 20 anos'.format(menor))
