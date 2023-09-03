a = [1 for i in range(26)]
c = 0
s = input()
for l in s:
        if a[ord(l)-97]:
                c += 1
                a[ord(l)-97] = 0
print(c)