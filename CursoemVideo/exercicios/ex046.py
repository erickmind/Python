import time
print('{:=^40}'.format(' CONTAGEM REGRESSIVA! '))
time.sleep(0.5)
print('{: ^40}'.format(' PREPARANDO CONTAGEM... '))
for i in range(10, -1, -1):
    time.sleep(1)
    print(i)
print('BOOM')

