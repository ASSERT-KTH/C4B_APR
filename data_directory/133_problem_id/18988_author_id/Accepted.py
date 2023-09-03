s = [int(i) for i in input().split(' ')]
t = [int(i) for i in input().split(' ')]

#s = [4,4,0]
#t = [2,1,2]
#s = [5,6,1]
#t = [2,7,2]
#s = [3,3,3]
#t=[2,2,2]

d = [a-b for a,b in zip(s,t)]
#print(d)

for i,_ in enumerate(d):
    if d[i] < 0:
        for j,_ in enumerate(d):
            while d[j] > 1 and d[i] < 0:
                d[j] -= 2
                d[i] += 1

worked = True
for i in d:
    if i < 0:
        worked = False
        break

if worked:
    print('Yes')
else:
    print('No')