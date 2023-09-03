n = int(input())
week = list(map(int, input().split()))
s = 0; i = 0
while s < n:
	s = s+week[i]
	if i == 6:
		i = 0
	else:
		i +=1
if i == 0:
        print(7)
else:
        print(i)