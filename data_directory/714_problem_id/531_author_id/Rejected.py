'''input
6 6 5 8 9
'''
l1, r1, l2, r2, k = map(int, input().split())
l = max(l1, l2)
r = min(r1, r2)
print(r-l+1 if k < l or k > r else r-l)