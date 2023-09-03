digits = [2, 3, 5, 6]
string = input()
numbers = string.split(" ")
for x in range(4):
    numbers[x] = int(numbers[x])
count = {digits[x]: numbers[x] for x in range(4)}
maximum = 0
results = "yes"
while results == "yes":
    if count[2] > 0 and count[5] > 0 and count[6] > 0:
        count[2] -= 1
        count[5] -= 1
        count[6] -= 1
        maximum += 256
    else:
        results = "no"
results = "yes"
while results == "yes":
    if count[3] > 0 and count[2] > 0:
        count[3] -= 1
        count[2] -= 1
        maximum += 32
    else:
        results = "no"
print(maximum)