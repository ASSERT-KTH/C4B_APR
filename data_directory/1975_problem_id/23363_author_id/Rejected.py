n, t=map(int, input().split(' '))
queue=input()
people=[]
for i in queue:
    people.append(i)
for j in range(t):
    i=0
    while(i<n):
        if (people[i]=='B' and people[i+1]=='G'):
            t=people[i]
            people[i]=people[i+1]
            people[i+1]=t
            i+=2
        else:
            i+=1
result=''
for i in people:
    result+=i
print(result)