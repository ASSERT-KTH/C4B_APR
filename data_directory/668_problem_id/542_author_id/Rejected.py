n = int(input())
for i in range(n):
  if i % 2:
    print('I love')
  else:
    print('I hate')
  if i + 1 < n:
    print('that')
  else:
    print('it')