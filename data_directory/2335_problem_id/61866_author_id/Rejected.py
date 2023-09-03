s = input()
cmp = ['h','e','l','l','o']
for i in s :
    if(i == cmp[0]):
        cmp.pop(0)
print(['NO','YES'][cmp == []])