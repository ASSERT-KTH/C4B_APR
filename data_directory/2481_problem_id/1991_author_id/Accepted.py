n = int(input())
r = 1
while r * 5 < n:
    n -= r * 5
    r *= 2

names = ("Sheldon", "Leonard", "Penny", "Rajesh", "Howard");
print(names[int((n - 1) / r)])