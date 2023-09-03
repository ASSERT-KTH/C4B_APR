word = input()

goalCount = 0
prev = word[0]

for w in word:
    if w == prev:
        goalCount += 1
    else:
        goalCount = 0
    if goalCount == 7:
        print("YES")
        exit()
    prev = w
print("NO")