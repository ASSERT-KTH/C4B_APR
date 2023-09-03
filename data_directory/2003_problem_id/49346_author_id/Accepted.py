i = int(input())
y=list()
x=list()
f=1
while y!=x or f==1:
    f=0
    i+=1
    a = str(i)
    x = list()
    y=list()
    for j in range(0,len(a)):
        x.append(a[j])
    y = sorted(set(x))
    x = sorted(x)
    if y==x:
        print(i)
        break