expr = str(input('Digite uma expressão qualquer: '))
#lparen = 0
#rparen = 0
pilha = []

'''for i in expr:
    if i == '(':
        lparen += 1
    elif i == ')':
        rparen += 1'''
for i in expr:
    if i  == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[32mA expressão está correta!\033[m')
else:
    print('\033[31mA expressão está errada!\033[m')
