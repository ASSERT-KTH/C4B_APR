a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
t = [0 for x in range(e)]
for y in range(0, e, a):
    t[y]=1
for y in range(0, e, b):
    t[y]=1
for y in range(0, e, c):
    t[y]=1
for y in range(0, e, d):
    t[y]=1
ret = 0
for y in t:
    if y==1:
        ret+=1
print (ret)