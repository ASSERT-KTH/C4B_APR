n=0
def rec (i):
   global n
   j=i*10+4
   k=i*10+7
   #print (j," ",k)
   if j>n and k>n: return False
   if n%k==0 or n%j==0:return True
   if j<n and k<n : return rec(j) or rec(k)
   if j<n: return rec(j)
   if k<n:return rec(k)

n=int(input())
if(rec(0)):print("YES")
else:print("NO")