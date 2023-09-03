x=int(input())
k=0
i=1
while i*i<=x:
    if x%i==0:k+=bool(set(str(x)).__rand__(set(str(i))))
    i+=1
print(k+bool(x-1))