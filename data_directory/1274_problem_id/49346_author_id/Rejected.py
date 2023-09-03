k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
cnt=0
for i in range(0,d):
	if i%k==0 or i%l==0 or i%m==0 or i%n==0:
		cnt+=1
print(cnt)