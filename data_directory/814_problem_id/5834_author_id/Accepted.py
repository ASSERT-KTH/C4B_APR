numbers = [int(x) for x in input().split(" ")]

a = numbers[0]
b = numbers[1]

for i in range(1, 100000):
    if (a*i - b)%10 == 0 or a * i % 10 == 0:
        print(i)
        break