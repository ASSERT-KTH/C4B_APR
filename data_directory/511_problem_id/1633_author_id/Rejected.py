string = input()
numbers = string.split(" ")
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
if c != 0:
    if abs(c) == c:
        while a < b:
            a += c
    else:
        while a > b:
            a += c
if a == b:
    results = "YES"
else:
    results = "NO"
print(results)