"""x=int(input())
i=1
while 1:
    y=x
    y=(y-(2*i))/2
    if y<=i:
        break
    i+=1
i-=1
print(i)
"""
n=int(input())
if(n%2==1):
    print(0)
else:
    m=n//2
    if(m%2==0):
        m-=1
    print(m//2)