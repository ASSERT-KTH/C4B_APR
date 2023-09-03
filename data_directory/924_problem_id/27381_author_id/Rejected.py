# n, m e k

s = input().split()

n = int(s[0])
m = int(s[1])
k = int(s[2])

j = int((k - 1) / (2 * m))
i = int(((k - 1) % (2 * m)) / 2)

print(str(j + 1) + " " + str(i + 1), end = " ")
if i % 2 == 1:
    print('L')
else:
    print('R')