a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = [0 for x in range(e)]
for y in range(a-1, e, a):
    t[y]=1
for y in range(b-1, e, b):
    t[y]=1
for y in range(c-1, e, c):
    t[y]=1
for y in range(d-1, e, d):
    t[y]=1
ret = 0
for y in t:
    if y==1:
        ret+=1
print (ret)