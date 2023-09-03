n = int(input())
s = "aabb"
a = len(s)
print(s * (n // a) + s[:n % a])