n=int(input())
a=""
if n%2 and n>=3:n-=3;a+='7'
while n>0:n-=2;a+='1'
print(a)