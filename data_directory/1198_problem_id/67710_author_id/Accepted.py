import sys
string = input()
instruction = {"H":1, "Q":1, "9":1}
for i in range(len(string)):
    if instruction.get(string[i]):
        print("YES")
        sys.exit()
print("NO")