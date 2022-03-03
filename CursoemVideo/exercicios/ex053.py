print('{:=^40}'.format('DETECTOR DE PALÍNDROMOS'))
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
flag = True

for i in range(0, len(frase)//2):
    if frase[i] != frase[len(frase)-1-i]:
        flag = False

if flag == False:
    print('A frase NÃO É um palíndromo!')
else:
    print('A frase É um palíndromo!')
