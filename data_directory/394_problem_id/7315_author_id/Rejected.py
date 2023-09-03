s = input()
com = -1
cn = [-1]
for c in s:
    while com != -1 and c != s[com]:
        com = cn[com]
    com += 1
    cn.append(com)
lenth = cn[-1]
if cn.count(lenth) < 2:
    lenth = cn[lenth]
print(s[:lenth] if lenth > 0 else "Just a legend")