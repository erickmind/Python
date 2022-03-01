dist = int(input('Digite a distância da viagem: '))
if dist <= 200:
    print('O preço da passagem será de R${:.2f}!'.format(dist*0.5))
else:
    print('O preço da passagem será de R${:.2f}!'.format(dist*0.45))
