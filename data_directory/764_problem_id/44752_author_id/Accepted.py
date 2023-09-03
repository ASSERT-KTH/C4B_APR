l = [int(x) for x in input().split()]

#for i in range(3):
#	l.append(input())

l.sort()

mid = l[1]

ans = 0;

for i in range(3):
	ans += abs(int(mid) - int(l[i]))

print(ans)