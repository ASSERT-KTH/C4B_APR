import math
string = input()
numbers = string.split(' ')
a = int(numbers[0])
b = int(numbers[1])
solutions = 0
for x in range(int(math.sqrt(a)) + 1):
    y = a - x ** 2
    if x + y ** 2 == b:
        solutions += 1
print(solutions)