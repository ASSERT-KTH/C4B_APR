s = input()
t = [s[i] for i in range(len(s)//2) if s[i] != s[len(s) - i - 1]]
print(['NO', 'YES'][(len(t) <= 1 and len(s) % 2 == 1) or len(t) == 1])