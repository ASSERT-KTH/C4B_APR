n = int(input())
s = "abbc"
a = len(s)
print(s * (n // a) + s[:n % a])