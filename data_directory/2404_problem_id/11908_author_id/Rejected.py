l=[]
for i in range (8):
    l.append(input())

c=0
for i in range (8):
    for j in range (8):
        if l[i][j]=='W':
            c+=1
            break
        
for i in range (8):
    for j in range (8):
        if l[j][i]=='W':
            c+=1
            break
print(16-c)