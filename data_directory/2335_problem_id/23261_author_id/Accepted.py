text = input()
j = 0
tmp = ''
solution = False
flags = [True, False, False, False, False, False]
target_chars = ['', 'h', 'e', 'l', 'l', 'o']
searchable_chars = ['h', 'e', 'l', 'o']


for x in text:
    if x in searchable_chars:
        tmp += x
text = tmp


for i in range(len(text)):
    if flags[0] and flags[1] and flags[2] and flags[3] and flags[4]:
        solution = True
        break
    else:
        if text[i] == target_chars[j] and text[i] != 'l':
            continue
        elif text[i] == target_chars[j + 1]:
            j += 1
            flags[j] = True  # Swap
        # else:
        #    for x in flags:
        #        x = False
        #    j = 0


if solution:
    print('YES')
else:
    print('NO')