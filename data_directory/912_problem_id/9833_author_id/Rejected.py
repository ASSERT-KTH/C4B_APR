n,k=input().strip().split(' ')
n,k=[int(n),int(k)]
t_p=240-k
x=(t_p-(t_p%5))//5
j=0
sum1=0
while sum1!=x:
      sum1+=j
      j+=1
if j<n:
      print(j-1)
else:
      print(n)