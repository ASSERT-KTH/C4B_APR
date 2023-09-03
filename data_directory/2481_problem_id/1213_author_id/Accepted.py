from math import sqrt
n = int(input())
for i in range(1,100):
    if 2**i>=(n/5+1):
        a = i-1
        break
c = int(((n - (2**a-1)*5)+2**a-1)/2**a)
    
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