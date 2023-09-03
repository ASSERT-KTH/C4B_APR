k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
dragons = 0
for x in range(1, d + 1):
    if x % k == 0:
        results = "yes"
    elif x % l == 0:
        results = "yes"
    elif x % m == 0:
        results == "yes"
    elif x % n == 0:
        results = "yes"
    else:
        results = "no"
    if results == "yes":
        dragons += 1
print(dragons)