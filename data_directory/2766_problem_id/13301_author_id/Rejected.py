s = input()
print('YES' if sum(s[i] != s[-i - 1]  for i in range(len(s) // 2)) <= 1 else 'NO')