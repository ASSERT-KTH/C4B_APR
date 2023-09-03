h,m=map(int,input().split(":"))
m+=int(input())
h=(h+m//60)%24
m=m%60
f=lambda x:"0"*(not x//10)+str(x)
print(f(h)+":"+f(m))