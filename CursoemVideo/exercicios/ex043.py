altura = float(input('Digite a altura da pessoa (m): '))
peso = float(input('Digite o peso da pessoa (kg): '))
imc = peso/(altura ** 2)

print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[33mAbaixo do peso!\033[m')
elif imc < 25:
    print('\033[32mPeso ideal\033[m')
elif imc < 30:
    print('\033[33mSobrepeso\033[m')
elif imc < 40:
    print('\033[33mObesidade\033[m')
else:
    print('\033[31mObesidade mórbida\033[m')