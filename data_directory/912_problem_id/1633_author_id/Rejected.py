string = input()
numbers = string.split(" ")
minutes = int(numbers[1])
total = 0
i = 0
while total <= 240 - minutes:
    i += 1
    total += i * 5
print(i - 1)