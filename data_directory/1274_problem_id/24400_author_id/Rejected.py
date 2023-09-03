from fractions import gcd
initial=[]
num=0
count=0
for j in range(0,5):
    initial.append(int(input()))
for i in range(1,initial[4]+1):
            if gcd(i,initial[0])==1 and gcd(i,initial[1])==1 and gcd(i,initial[2])==1 and gcd(i,initial[3])==1:
                num+=1

for k in range(0,4):
    if initial[k]==1:
        count+=1
if count>0:
    print(initial[4])
else:
    print(int(initial[4]-num))