str = input()
s = str
n = ['h', 'e', 'l', 'o']
for i in str:
	if i not in n:
		s = s.replace(i, "")
count = []
str = ""

for i in n:
    count.append(s.count(i))

li = list(s)

for i in range(len(count)):
	if n[i] != 'l':
		for j in range(count[i] - 1):
			li.remove(n[i])
	else:
		for j in range(count[i] - 2):
			li.remove('l')

if "".join(li) == 'hello':
	print("YES")
else:
	print("NO")