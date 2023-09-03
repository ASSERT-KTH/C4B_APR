from sys import stdin, stdout

w = int(stdin.readline())

if w > 2 and w % 2 == 0:
    stdout.write("YES")
else:
    stdout.write("NO")

# 1502317526709