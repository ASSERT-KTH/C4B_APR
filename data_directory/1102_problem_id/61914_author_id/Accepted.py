s = input()
vowels = ['a', 'i', 'u', 'e', 'o', 'y']
res = ''
for c in s:
  if c.lower() not in vowels:
    res += '.'+c.lower()
print(res)