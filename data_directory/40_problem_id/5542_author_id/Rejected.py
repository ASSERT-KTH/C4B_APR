n=int(input())
for i in range (210,n+1):
    if n%i==0:
        while n%(i**2)!=0:
            print (i)