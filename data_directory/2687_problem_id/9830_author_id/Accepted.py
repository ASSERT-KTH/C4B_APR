# MAX_INT = 1000000000
# (n,m) = map(int, input().split())

# if n <= m:
#     print n
# else:
#     M = m
#     n -= m
#     l = 0
#     r = MAX_INT
#     while (l < r):
#         m = (l + r)/2
#         val = m * (m+1)/2
#         if val >= n:
#             r = m
#         else:
#             l = m+1
#     print l + M

(n, m) = map(int, input().split())
if n <= m:
	print(n)
else:
	aM = m
	n -= m
	(l, r) = (0, int(2e9))
	while l < r:
		m = (l + r) // 2;
		val = m * (m+1) // 2;
		if val >= n:
			r = m
		else:
			l = m+1
	print(l + aM)