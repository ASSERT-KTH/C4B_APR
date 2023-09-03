n=int(input())
a=int(input())
b=int(input())
c=int(input())
if a<=b-c or n<b: print(n//a)
else:
    print((n-c)//(b-c)+((n-c)%(b-c))//a)