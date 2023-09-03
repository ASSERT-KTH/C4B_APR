import math
(x,y,l,r) = (int(i) for i in input().split())

vvrs = []

for i in range(60):
	for j in range(60):
		cur = x**i + y**j
		if cur>r: break
		if cur>=l: 
			vvrs.append(cur)

vvrs.sort()
maxcnt = 0
for i in range(len(vvrs)-1):
	rzn = vvrs[i+1]-vvrs[i]
	if rzn>maxcnt: maxcnt = rzn

if len(vvrs)==0:
	print(r-l+1)
else:
	print(max(maxcnt-1,vvrs[0]-l, r-vvrs[-1]))