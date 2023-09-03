#http://codeforces.com/problemset/problem/825/A

len = int(input())
code = input()
cont = 0
result = ""

for i in range(len):
    if code[i] == "0":
        if cont != 0:
            result += str(cont)
            cont = 0
        else:
            result += "0"
    elif code[i] == "1":
        cont += 1

if cont != 0:
    result += str(cont)

print(result)