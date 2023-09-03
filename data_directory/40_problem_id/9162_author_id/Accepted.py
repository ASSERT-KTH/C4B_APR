n=int(input())
for i in range (2,10**6):
    while n % (i**2)==0:
        n=n//i
print(n)