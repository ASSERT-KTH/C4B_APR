n = int(input())
if(n % 2 == 1):
    print(7, end='')
    n -= 3
while(n > 1):
    print(1, end='')
    n -= 2