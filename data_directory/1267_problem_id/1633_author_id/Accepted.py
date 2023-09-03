a = int(input())
a //= 2
n = input()
results = "NO"
condition = True
for x in n:
    if x != "4" and x != "7":
        condition = False
        break
if condition:
    x = sum(map(int, list(n[:a])))
    y = sum(map(int, list(n[a:])))
    if x == y:
        results = "YES"
print(results)