n = int(input())
if n > 5 and n % 5 != 0:
    print(int(n / 5 + 1))
elif n <= 5:
    print("1")
else:
    print(int(n / 5))