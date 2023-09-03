n=int(input())
y=n
k=2
p=0
for q in range (0, n-2):
        n=y
        while n>1:
                a=n%k
                n=n//k
                p=p+a
        p=p+n        
        k=k+1
t=k-2
print(str(p)+"/"+str(t))