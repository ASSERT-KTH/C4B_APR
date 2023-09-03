a=int(input())
f=a
c=0
for i in range (2,a):
    a=f
    while a>=i:
        b=a%i
        a-=b
        c+=b
        a=a/i
    c+=a
d=f-2
print('%d/%d'%(c,d))