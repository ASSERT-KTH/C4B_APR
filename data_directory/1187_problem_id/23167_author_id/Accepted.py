s = input()
print(s.swapcase() if s[1:].isupper() or len(s)==1 else s)