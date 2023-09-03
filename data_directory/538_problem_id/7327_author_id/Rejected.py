mat = list(map(int, input().split()))
sat=[]
d = {}

for i in mat:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for j in d:
    if d[j]>3:
        d[j]=3
    if d[j]>1:
        sat.append(j * d[j])

print(sum(mat) - max(sat))