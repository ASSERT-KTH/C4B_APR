a,b,c,d,e,f = map(int, input().split())
if (a*c*e==0 and (f>0 or d>0)) or (b*d*f > a*c*e>0 ):
    print("Ron")
else:
    print("Hermione")