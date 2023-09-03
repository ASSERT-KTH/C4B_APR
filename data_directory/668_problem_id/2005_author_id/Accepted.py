odd = 'I hate'
even = 'I love'
interm = ' that '
n = int(input())
for i in range(n):
    i += 1
    if i > 1:
        print(interm,end='')
    if i % 2 == 1:
        print(odd,end='')
    if i % 2 == 0:
        print(even,end='')
    if i == n:
        print(' it')