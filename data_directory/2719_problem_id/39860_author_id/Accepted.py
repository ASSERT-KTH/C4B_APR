l,b = [int(x) for x in input().split()]

n = 0

while b >= l:
    n+=1
    l=3*l
    b = 2*b

print(n)