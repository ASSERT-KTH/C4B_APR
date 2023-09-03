l=list(map(int,input().split(" ")))
l.sort()
a=l[0]
b=l[1]
c=l[2]
one=a+b+c
two=2*(a+b)
print(min(one,two))