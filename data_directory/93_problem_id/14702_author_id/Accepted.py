k,a,b=input().split(' ')
k=int(k)
a=int(a)
b=int(b)
if a%k!=0 :
    a=a+k-a%k
print(max(0,1+(b-a)//k))