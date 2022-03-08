num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei {v}!')

a = [1, 2, 3, 4]
b = a[:]
c = a
print(a)

c[0] = 10
b[0] = 7

print(a)
print(b)
print(c)

