def bigbang(stack, s):
    for i in range(s):
        a=stack.pop(0)
        stack.append(a)
        stack.append(a)
    return a

s = int(input())
print(bigbang(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], s))