n,m,a=map(int,input().split())
print(((n//a)+(n%a>0))*((m//a)+(m%a>0)))