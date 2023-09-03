# import sys

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
dividers = [k, l, m, n]

siev = range(d)
i = 1
S = 0

for i in siev:
    for j in dividers:
        if i % j == 0:
            S += 1
            break

print(S)
# if (k == 1 or l == 1 or m == 1 or n == 1):
#     print(d)
#     sys.exit()


# S = sum([(d // i) for i in dividers])
# s = []

# i = 0
# while i < len(dividers) - 1:
#     j = i + 1
#     while j < len(dividers):
#         s.append(dividers[i] * dividers[j])
#         j += 1
#     i += 1

# s = sum([d // i for i in s])

# print(S - s)