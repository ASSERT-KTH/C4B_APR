"""satr=[int(x) for x in input().split(" ")]"""
satr=input()
S=0
koor=1
for i in satr:
    if i=='A' or i=='E' or i=='I' or i=='U' or i=='O' or i=='Y':
        if koor>S:
            S=koor
        koor=0
    koor+=1
print(str(S))