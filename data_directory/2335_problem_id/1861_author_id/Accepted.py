hello = "hello"
s = input();
count = 0
for c in s:
    if count == 5:
        break
    else:
        if c == hello[count]:
            count += 1
print("YES" if count == 5 else "NO")