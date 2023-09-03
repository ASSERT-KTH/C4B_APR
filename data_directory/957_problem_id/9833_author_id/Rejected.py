def f(list4):
    col=['R','B','Y','G']
    a=list4.index('!')
    for j in col:
        if j not in list4:
            list4[a]=j
    return list4
s=str(input())
l=list(s)
list1=['R','B','Y','G']
ans=[0,0,0,0]
while l.count('!')>0:
    i=0
    while l[i:i+4].count('!')==0 or l[i:i+4].count('!')!=1:
        i+=1
        #print(i)
    list3=f(l[i:i+4])
    #print(list3,l[i:i+4])
    for j in range(4):
        if list1[j] not in l[i:i+4] and list1[j] in list3:
            ans[j]+=1
            #print(list1[j])
    l[i:i+4]=list3
print(*ans)