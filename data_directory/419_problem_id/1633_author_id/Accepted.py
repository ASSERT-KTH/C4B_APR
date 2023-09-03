string = input()
numbers = string.split(" ")
n = int(numbers[0])
a = int(numbers[1])
b = int(numbers[2])
x = abs(a + b % n)
if x % n == 0:
    print(n)
else:
    print(x % n)