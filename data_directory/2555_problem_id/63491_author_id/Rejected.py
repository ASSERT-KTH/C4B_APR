b = input()
count = 0
for i in range(len(b) - 1):
    if b[i] == b[i+1]:
        count += 1
    else:
        count = 0
    if count > 6:
        break
if count < 7:
    print("NO")
else:
    print("YES")