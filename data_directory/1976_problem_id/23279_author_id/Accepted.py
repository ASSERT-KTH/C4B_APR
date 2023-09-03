n = int(input())
s = input()
c = []
count = 0
m = s[0]
for i in range(n):
    if s[i] == m:
        count += 1
    else:
        c.append(count)
        m = s[i]
        count = 1
c.append(count)
num = 0
for i in c:
    if i>1:
        num += i-1
print(num)