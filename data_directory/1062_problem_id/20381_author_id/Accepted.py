import sys
no=str(input())
d={}
d['4']=0
d['7']=0
for i in no:
	if i=='4' or i=='7':
		d[i]+=1
sum1=0
sum1+=d['4']
sum1+=d['7']
li=['4','7']
for i in str(sum1):
	if i not in li:
		print("NO")
		sys.exit()
print("YES")