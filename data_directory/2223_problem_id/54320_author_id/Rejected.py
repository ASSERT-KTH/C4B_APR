w=int(input())
x=w
n=0
for i in range(0,w//2+2):
    if i%2==0 and x%2==0 :
         print('YES')
         n+=1
         break 
    x-=1
if n==0 : print('NO')