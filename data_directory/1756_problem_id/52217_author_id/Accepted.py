'''
CF problem 228A
@autor Yergali B
'''
a=sorted(list(map(int,input().split())))
b=[]
c=0
for i in range(4):
    for j in range(4):
        if a[i]!=a[j]:
            c+=1
    b.append(c)
    c=0
#print(b)
if max(a)==min(a):
    print(3)
elif max(b)==min(b)==2:
    print(2)
else:
    print(3-min(b))