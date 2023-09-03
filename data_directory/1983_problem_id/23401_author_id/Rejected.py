from sys import stdin
i = int(stdin.readline().rstrip())
if i == 1:
    clicks = 1
else:
    clicks = 0
    current_error = 1
    for x in range(2,i+1):
        clicks += x
        clicks += current_error
        current_error *= (x-1)
print (clicks)