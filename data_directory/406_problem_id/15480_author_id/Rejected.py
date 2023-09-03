s = input()
res = 0
for i in s:
    if i.islower():
        res -= ord(i) - ord("a") + 1
    else:
        res += ord(i) - ord("A") + 1
print(res)