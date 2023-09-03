l,b = map(int, input().split())
i=0
while b>=l:
    l*=3
    b*=2
    i+=1
print(i)