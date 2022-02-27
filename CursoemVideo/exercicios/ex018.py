import math
val = int(input('Digite o valor do ângulo: '))

print('O valor do seno é: {:.2f}\nO valor do cosseno é: {:.2f}\nO valor da tangente é: {:.2f}'
      .format(math.sin(math.radians(val)), math.cos(math.radians(val)), math.tan(math.radians(val))))
