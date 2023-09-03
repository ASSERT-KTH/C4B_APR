#number_of_drinks = int(input())
numbers = [int(x) for x in input().split(" ")]

limaks_spare_time = 240 - numbers[1]
solving_time = 0

for i in range(1, numbers[0] + 1):
    solving_time += 5*i
    if solving_time > limaks_spare_time:
        print(i-1)
        break
if solving_time < limaks_spare_time:
    print(numbers[0])