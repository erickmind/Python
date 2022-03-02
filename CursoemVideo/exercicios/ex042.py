l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[32mÉ possível formar um triângulo com os lados inseridos!\033[32m')
    if l1 == l2 == l3:
        print('\033[33mO triângulo será um triângulo Equilátero!\033[m')
    elif l1 != l2 != l3 != l1:
        print('\033[33mO triângulo será um triângulo Escaleno!\033[m')
    else:
        print('\033[33mO triângulo será um triângulo Isósceles\033[m')
else:
    print('\033[31mNão é possível formar um triângulo com os lados inseridos!\033[m')
