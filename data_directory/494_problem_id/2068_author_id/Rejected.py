n=int(input())
a=list()
for i in range(1,272):
    a.append(str(i))
s="".join(a)
print(s[n-1])