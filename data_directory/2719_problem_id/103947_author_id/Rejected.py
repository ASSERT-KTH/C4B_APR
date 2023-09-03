a,b = input("Enter two numbers here: ").split()
i=0;
a=int(a)
b=int(b)
while  a>b or a<1 or b>10:
    print("erreur dans les données initiales resaisissez les poids")
    a,b = input("Enter two numbers here: ").split()
    i=0;
    a=int(a)
    b=int(b)
while (a<=b):
        a=a*3
        b=b*2
        i=i+1
print(i)