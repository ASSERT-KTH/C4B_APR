s=input()
i=0
ans = 0
n = len(s)
while i<n:
	if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='Y'):
		l=1
		i+=1 
		while(i<n and s[i]!='A' and s[i]!='E' and s[i]!='I' and s[i]!='O' and s[i]!='U' and s[i]=='Y'):
			i+=1
			l+=1
		ans = max(ans,l)
	else:
		l=1
		while(i<n and s[i]!='A' and s[i]!='E' and s[i]!='I' and s[i]!='O' and s[i]!='U' and s[i]=='Y'):
			i+=1
			l+=1
		ans = max(ans,l)
print(ans)