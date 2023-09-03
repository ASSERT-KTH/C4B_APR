word = input()
last = 3
count = 0
for i in word:
  if last == i:
    count += 1
    if count > 6:
      print("YES")
      quit()
  else:
    count=0
  last = i
print("NO")