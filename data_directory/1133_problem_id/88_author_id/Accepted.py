a=input()
x=a.count('4')
y=a.count('7')

if y==x==0:
    print(-1)
elif y>x:
    print(7)
else:
    print(4)