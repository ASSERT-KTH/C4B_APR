a , b= map(int,input().split())
x= 1
while 0!=a*x%10 !=b :
    x=x+1
print(x)