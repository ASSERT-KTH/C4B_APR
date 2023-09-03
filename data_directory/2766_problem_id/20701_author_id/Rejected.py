s = input()
print(['YES', 'NO'][len([s[i] for i in range(len(s)//2) if s[i] != s[len(s) - i - 1]]) != 1])