n,a,b=map(str, input().split())
n=int(n)
if b=="week":
    if n==5 or n==6:
        print(53)
    else:
        print(52)
else:
    if n==31:
        print(7)
    elif n>28 and n<=30:
        print(11)
    else:
        print(12)