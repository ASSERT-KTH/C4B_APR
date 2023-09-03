from sys import stdin
a,b,c = map(int,stdin.readline().split())


if((a != b and c == 0) or (b > a and c < 0) ):
    print("NO")
elif( (a == b )  or ( b > a and c > 0 and ((b-a)% c == 0))  or( a > b and c < 0 and ((a-b)%c ==0))):
    print("YES")
else:
    print("NO")