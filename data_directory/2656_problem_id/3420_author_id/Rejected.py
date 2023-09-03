n, k = input().split()
k = int(k)
remove = 0
n = str(n)
for i in range(n.__len__()-1,-1,-1):
    if k<=0:
        break
    if n[i]=='0':
        k-=1
    else:
        remove+=1

print(remove)