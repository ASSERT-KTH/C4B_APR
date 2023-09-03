n = int(input())

print("I hate", end =" ")


for i in range(n):
    if i % 2 == 0:
        print("that I love", end =" ")
    elif i % 2 != 0:
        print("that I hate", end =" ")
print("it")