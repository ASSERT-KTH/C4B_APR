k2,k3,k5,k6=map(int,input().split())
table={2:k2,3:k3,5:k5,6:k6}
tot=0
while(table[2]!=0 and table[5]!=0 and table[6]!=0):
    tot+=256
    table[2]-=1
    table[5]-=1
    table[6]-=1
while(table[2]!=0 and table[3]!=0):
    tot+=32
    table[3]-=1
    table[2]-=1
print(tot)