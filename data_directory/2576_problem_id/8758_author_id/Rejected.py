temp=input()
k,a,b =map(int,temp.split(" "))

if a<k and b<k :
    print(-1)
else:
    print(a//k + b//k)