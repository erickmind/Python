def area(a, b):
    print(f'A área é {a*b}m²')

print(f'{" Calculadora de terrenos ":=^40}')
comp = float(input('Digite o comprimento do terreno: '))
larg = float(input('Digite a largura do terreno: '))
area(comp, larg)
