from collections import deque
l = ['Sheldon','Leonard','Penny','Rajesh','Howard']
dq = deque([0,1,2,3,4])
n = int(input().strip())
e = ''
for _ in range(n):
    e = dq.popleft(); dq.extend([e,e])
print(l[e])