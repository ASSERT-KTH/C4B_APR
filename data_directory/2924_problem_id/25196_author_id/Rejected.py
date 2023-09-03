n = int(input())
s = input()

current_num = 0

for el in s:
    if el == '1':
        current_num += 1
    else:
        print(current_num, end='')
        current_num = 0

if current_num != 0:
    print(current_num)