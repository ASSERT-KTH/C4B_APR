def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a,s=input().split()
i=int(a)+1
s=int(s)
v=int(a)
while i<=s:
    if isprime(i):
        v=i
        break
    i+=1
if v==s and isprime(s):
    print ("YES")
else:
    print ("NO")