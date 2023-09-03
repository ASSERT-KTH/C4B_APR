a,b = input().split()
i=0;
a=int(a)
b=int(b)
i=int(i)
if  a>b or a<1 or b>10:
    print("erreur dans les données initiales")
else:
    while (a<=b):
        a=a*3
        b=b*2
        i=i+1
print(i)