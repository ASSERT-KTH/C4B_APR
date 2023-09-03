string = input()
numbers = string.split(" ")
a = int(numbers[0])
b = int(numbers[1])
if abs(a - b) <= 1:
    print("YES")
else:
    print("NO")