def start_check(a):
    n = a % 4
    if n==2:
        return 4
    elif n==3:
        return 2
    elif n==0:
        return 6
    else:
        return 8

n = int(input())
if n==0:
    print(1)
else:
    print(start_check(n))