import sys
players=int(sys.stdin.readline().strip('\n'))
count=1
total=1
while True:
    if (players-1)-(total)>0:
        count+=1
        total+=count
    else:
        print(count)
        break