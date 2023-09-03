s = input().lower()
s2 = ""
v= "aoyeui"
i = 0
while i < len(s):
    if s[i] in v:
        s2 += '.'
    else:
        s2 += s[i]
    i += 1
print(s2)