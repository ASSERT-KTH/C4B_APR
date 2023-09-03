string = input()
numbers = string.split()
x = int(numbers[0])
y = int(numbers[1])
n = 6 - max([x, y]) + 1
print(str(n) + "/6")