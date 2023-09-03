a=list(map(int,input().split()))

a.sort()

afstand=abs(a[0]-a[1])+abs(a[2]-a[1])

print(afstand)