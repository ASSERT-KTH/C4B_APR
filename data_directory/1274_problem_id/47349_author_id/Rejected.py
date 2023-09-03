k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
w=0
for x in range(1, d):
    if x%k==0 or x%l==0 or x%m==0 or  x%n==0:
        w+=1

if k>d and l>d and m>d and n>d:
    w=0
print(w)