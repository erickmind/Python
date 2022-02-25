nome = input('Qual é o seu nome? ')

print('Prazer em te conhecer {:>20}'.format(nome))  #  À direita de 20 espaços
print('Prazer em te conhecer {:<20}'.format(nome))  # À esquerda de 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome))  # Centralizado entre espaços em branco
print('Prazer em te conhecer {:=^20}!'.format(nome))  # Centralizado entre 20 =

val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
s = val1 + val2
m = val1 * val2
d = val1 / val2
di = val1 // val2
e = val1 ** val2

print('A soma é {},\no produto é {},\na divisão é {:.3f}'.format(s, m, d), end = ' > ')
print('A divisão inteira é {} e potência é {}'.format(di, e))
