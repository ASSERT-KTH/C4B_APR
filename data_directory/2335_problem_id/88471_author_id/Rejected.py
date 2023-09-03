import sys
s = input();
w = "hello"
k = 0
for i in s:
    if k == 5:
        print("YES")
        sysexit()
    if i == w[k]:
        k += 1
if k == 5:
    print("YES")
else:
    print("NO")