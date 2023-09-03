n, k = input().split()
n = int(n)
k = int(k)
sum = 0
if n == 1:
 print (sum)
elif n == 2:
 sum = 1
 print (sum)
else:
 for i in range(k):
   sum += 2*n -3
   n -= 2
   if n < 2:
     break
 print (sum)