import math

def main():
    a,b,c = map(int, input().split())
    if a<b:
        if c<=0:
            return "NO"
        else:
            if abs(b-a)%c==0:
                return "YES"
            else:
                return "NO"
    else:
        if a==b:
            return "YES"
        if c>=0:
            return "NO"
        else:
            if abs(b-a)%c==0:
                return "YES"
            else:
                return "NO"

print(main())