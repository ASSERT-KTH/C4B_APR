a,b,c=map(int,(input().split(" ")))
if(a<b<c):
    k=(c-b)+(b-a)
    print(k)
elif(b<a<c):
    k=(c-a)+(a-b)
    print(k)
elif(a<c<b):
    k=(b-c)+(c-a)
    print(k)
elif(c<b<a):
    k=(a-b)+(b-c)
    print(k)
elif(c<a<b):
    k=(b-a)+(a-c)
    print(k)
elif(b<c<a):
    k=(a-c)+(c-b)
    print(k)