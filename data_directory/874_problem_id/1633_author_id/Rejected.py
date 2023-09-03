string = input()
numbers = string.split()
a = int(numbers[0])
b = int(numbers[1])
sequence = []
for x in range(a):
    sequence += [x + 1] + sequence
print(sequence[b - 1])