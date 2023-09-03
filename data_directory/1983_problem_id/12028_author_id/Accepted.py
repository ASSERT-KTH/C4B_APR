n=int(input())
x=0
for j in range(2, n):
    x=x+(n-j)*j
print(x+n-1+n)