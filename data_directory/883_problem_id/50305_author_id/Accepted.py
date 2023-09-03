word = list(input())

comb = []
for i in range(len(word)):
	l = word[-1]
	del word[-1]
	word = [l] + word
	str1 = ''.join(word)
	comb.append(str1)

print(len(set(comb)))