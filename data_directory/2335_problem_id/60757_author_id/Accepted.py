s = input()
result = True
for c in "hello":
    ix = s.find(c)
    if ix == -1:
        result = False
        break
    s = s[ix + 1:]
if result:
	print("YES")
else:
	print("NO")