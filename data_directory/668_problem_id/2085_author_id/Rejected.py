a=int(input())
b=""
for r in range(1,a+1):
    if(r%2==1):
        b=b+"I hate that "
    else:
        b=b+"I love that "
print(b)