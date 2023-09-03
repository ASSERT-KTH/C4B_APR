numb = [0, 0, 1, 2, 2, 1]
#odd, then even
chart = [1, 0, 5, 2, 3, 4]
add = int(input())
start = int(input())
start = 2*start
if add % 2 == 0:
    start += 1
add = (add+chart[start])%6
print(numb[add])