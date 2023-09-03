a,b,n = [int(x) for x in input().split(' ')]

def addingdigits(a,b,n):
    t = 0
    for i in range(10):
        if (a*10+i) % b == 0:
            t = a * 10 + i
            break
    if t == a:
        return -1
    else:
        return t*pow(10,(n-1))

print(addingdigits(a,b,n))