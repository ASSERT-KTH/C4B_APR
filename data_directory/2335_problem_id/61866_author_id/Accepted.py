s = input()
cmp = ['h','e','l','l','o']
for i in s:
    if(i == cmp[0]):
        cmp.pop(0)
    if(cmp == []):
        break
print(['NO','YES'][cmp == []])