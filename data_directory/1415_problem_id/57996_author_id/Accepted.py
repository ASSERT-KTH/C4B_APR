a,b,m,r0=0,0,0,0
a,b,m,r0=map(int,input().split())
ri=r0
i=0
I={}
while (ri) not in I:
        I[ri]=i
        ri=(a*ri+b)%m
        i+=1
print (i-I[ri])