i = -1
j = 0
str = input()
for char in str:
    if char == '0' or char == '1':
        i += 1
        if i == 5:
            i = 0
            j += 1
        if char == '1':
            break
print(abs(2-i) + abs(2-j)-1)