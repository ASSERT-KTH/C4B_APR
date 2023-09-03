s=input().split()
a=int(s[0])
b=int(s[1])
n=int(s[2])
if n == 0:
    print(b)
elif b > 0:
    print((n+b)%a)
elif b < 0:
    print(abs(a-b)%n)