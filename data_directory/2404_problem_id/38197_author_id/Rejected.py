V=[input().count('B') for _ in range(8)]
cnt=0
for i in V:
    if i==8:
        cnt+=1
if min(V[0],V[7])!=8:
    cnt+=min(V[0],V[7])
print(cnt)