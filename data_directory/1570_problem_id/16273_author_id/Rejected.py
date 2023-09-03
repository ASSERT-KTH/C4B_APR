k,b,n,t=input().split()

k=int(k)
b=int(b)
n=int(n)
t=int(t)

x=1
for i in range(n):
    x=k*x+b
num=t
sec=0
while(num<x):
    num=k*num+b
    sec+=1

print(sec)