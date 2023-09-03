names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())
length_of_row, circle = 5, 0
while n > 0:
    n -= length_of_row
    length_of_row *= 2
    circle += 1
n += length_of_row // 2
print(names[n // 2 ** (circle - 1)])