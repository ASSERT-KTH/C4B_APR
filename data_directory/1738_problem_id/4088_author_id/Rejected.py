a,b,c=map(int,input().split())
s1=a*b
s2=b*c
s3=c*a
a=((s1*s3)//s2)**0.5
b=((s1*s2)//s3)**0.5
c=((s2*s3)//s1)**0.5
print(int(4*(a+b+c)))