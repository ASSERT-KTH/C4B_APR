k = int(input())
a =  list(map(int,input().split()))
a.sort()
count = 0
pos = len(a)-1
while(k >0 and pos>0 ):
   count = count + 1
   k = k - a[pos]
   pos = pos - 1
if(count<13 and k<=0):
 print(count)
else:
   print(-1)