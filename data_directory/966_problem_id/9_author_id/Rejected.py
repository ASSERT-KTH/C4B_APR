import sys
input = sys.stdin.readline

hobbits,pillows,bedspot = list(map(int, input().split()))

pillows -= hobbits

counter = 1
bottom = bedspot - 1
top = bedspot

while True:
    cat = top - bottom
    if cat <=pillows:
        pillows -= cat
        counter += 1
    else:
        break

    if bottom > 0:
        bottom-=1
    if top < hobbits:
        top+=1
print(counter)