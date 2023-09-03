n,m=[int(i) for i in input().split()]
d=n*(n+1)//2
dk=m//d
c=m-dk*d
i=1
while c>=i:
    c=c-i
    i=i+1
print(c)