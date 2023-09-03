string = input()
numbers = string.split(" ")
a = int(numbers[0])
b = int(numbers[1])
if abs(a - b) <= 1 and a + b != 0:
    print("YES")
else:
    print("NO")