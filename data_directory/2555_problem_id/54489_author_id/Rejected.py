count = 0
i = 1
arr =[]
k = input()
for j in k:
    arr.append(int(j))
while i <= len(arr) - 1:
    if arr[i] == arr[i-1]:
        count += 1
    else:
        count -= 1
    if count < 0:
        count = 0
    if count >= 6:
        print("YES")
        break
    i += 1
if count < 6:
    print("NO")