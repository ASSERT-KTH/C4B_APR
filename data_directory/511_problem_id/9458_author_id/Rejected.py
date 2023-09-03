a,b,c = map(int,input().split())
if c == 0: print("NO") if a != b else print("YES")
else:
	print("YES") if b >= a and (b-a)%c == 0 else print("NO")