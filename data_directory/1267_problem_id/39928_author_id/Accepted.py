num_digits = int(input())
digits = input()
u = set(digits)
l = len(u)
half = int(num_digits/2)

if l == 2 and '7' in u and '4' in u:
    if sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]]):
        print('YES')
    else:
        print("NO")
elif l == 1 and '7' in u:
    if sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]]):
        print('YES')
    else:
        print("NO")
elif l == 1 and '4' in u:
    if sum([int(x) for x in digits[0:half]]) == sum([int(x) for x in digits[half:]]):
        print('YES')
    else:
        print("NO")
else:
    print("NO")