#numbers = [int(x) for x in input().split(" ")]

string = ""
for i in range(int(input())):
    if i % 2 == 0:
        string += "I hate that "
    else:
        string += "I love that "
print(string[0:-5] + "it")