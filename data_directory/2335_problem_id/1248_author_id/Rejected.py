s = input()

counter = 0
hi = "hello"
for i in range(len(s)):
    if s[i] == hi[counter]:
        counter += 1
if counter >= 5:
    print("YES")
else:
    print("NO")