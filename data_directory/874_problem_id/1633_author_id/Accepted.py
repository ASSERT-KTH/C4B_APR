string = input()
numbers = string.split()
a = int(numbers[1])
n = 0
while a % 2 == 0:
    a /= 2
    n += 1
print(n + 1)