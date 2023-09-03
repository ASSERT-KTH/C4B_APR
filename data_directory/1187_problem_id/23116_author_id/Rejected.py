# http://codeforces.com/problemset/problem/131/A

s = input()

if s[0].islower() or s[1:].isupper():
  print(s.capitalize())
elif s.isupper():
  print(s.lower())
else:
  print(s)