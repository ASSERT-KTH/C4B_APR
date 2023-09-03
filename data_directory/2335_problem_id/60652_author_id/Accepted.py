s = input()
a = "hello"
k = 0
for i in s:
    if i == a[k]:
        k+=1
    if k == 5:
        print("YES")
        exit()

print("NO")