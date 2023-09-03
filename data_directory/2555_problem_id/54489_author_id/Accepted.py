count = 0
i = 0
arr =[]
k = input()
for a in k:
    arr.append(int(a))
while i < len(arr) - 1:
    i += 1
    if arr[i - 1] == arr[i]:
        count += 1
    if arr[i - 1] != arr[i]:
        count = 0
    if count >= 6:
        print("YES")
        break
if count < 6:
    print("NO")