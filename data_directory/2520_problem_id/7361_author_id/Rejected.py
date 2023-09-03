from fractions import Fraction
y, w= map(int, input().split());

a=6-y+1;

b=6;
if a==6:
    print("1/1");
else:
    print(Fraction(a,b));