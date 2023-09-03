word = input()
last = 3
count = 1
for i in word:
  if last == i:
    count += 1
    if count > 6:
      print("YES")
      quit()
  else:
    count=1
  last = i
print("NO")