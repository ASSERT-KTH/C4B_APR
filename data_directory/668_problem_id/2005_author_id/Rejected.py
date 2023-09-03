odd = 'I hate it'
even = 'I love it'
interm = ' that '
n = int(input())
for i in range(n):
    i += 1
    if i > 1 and i != n+1:
        print(interm,end='')
    if i % 2 == 1:
        print(odd,end='')
    if i % 2 == 0:
        print(even,end='')