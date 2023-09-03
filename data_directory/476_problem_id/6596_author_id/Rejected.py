n = int(input())
output = 0
while 1:
    n -= 1
    output += 1 if n >= 0 else 0
    n -= 2
    output += 1 if n >= 0 else 0
    if n < 0:
        break
print(output)