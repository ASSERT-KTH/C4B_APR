(a, b) = (int(i) for i in input().split())
(c, d) = (int(i) for i in input().split())

br = -1
for k in range(1000000):
	n = ((d-b+c*k)/a)
	if n>=0 and not n%1:
		br = k
		print(br)
		break
if br!=-1:
	print(d+c*br)
else:
	print(-1)