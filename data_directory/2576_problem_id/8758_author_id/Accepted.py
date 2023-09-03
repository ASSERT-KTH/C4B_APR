temp=input()
k,a,b =map(int,temp.split(" "))

if (a<k and b<k) or ( a<k and b%k!=0 ) or ( b<k and a%k!=0 ):
    print(-1)
else:
    print(a//k + b//k)