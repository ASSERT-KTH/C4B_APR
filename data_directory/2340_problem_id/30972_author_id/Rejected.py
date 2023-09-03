str = input()

n_lower = 0
n_upper = 0

for c in str: 
    if c.islower():
        n_lower += 1
    elif c.isupper():
        n_upper += 1

if n_lower > n_upper:
    print(str.lower())
else:
    print(str.upper())