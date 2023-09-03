# Cf 697A
inp = input().split()
s = eval(inp[1])
x = eval(inp[2]) - eval(inp[0])
if (x%s == 0 or ((x-1)%s == 0 and x-1 != 0)) and x >= 0:
    print("YES")
else:
    print("NO")