'''input
24648817341102 41165114064236 88046848035 13602161452932 10000831349205
'''
l1, r1, l2, r2, k = map(int, input().split())
l = max(l1, l2)
r = min(r1, r2)
if l > r:
	print(0)
else:
	print(r-l+1 if k < l or k > r else r-l)