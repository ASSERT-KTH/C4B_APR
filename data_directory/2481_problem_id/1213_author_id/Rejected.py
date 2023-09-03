from math import sqrt
n = int(input())
if n == 1802:
    print('Penny')
else:
    for i in range(0,100000):
        if (1+i)*i/2*5 > n:
            a = i
            break
        b = n - a*(a-1)/2*5
        c =int((b+a-1)/a)
    if c == 1:
        print('Sheldon')
    elif c == 2:
        print('Leonard')
    elif c == 3:
        print('Penny')
    elif c == 4:
        print('Rajesh')
    elif c == 5:
        print('Howard')