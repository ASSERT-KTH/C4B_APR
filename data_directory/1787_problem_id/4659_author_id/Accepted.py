import sys

permSize = int(input())

if permSize%2==1:
    print("-1")
    sys.exit()

odd = 1
even = 2

for i in range(permSize):
    if i%2==0:
        print(even,end=" ")
        even += 2

    else:
        print(odd,end=" ")
        odd += 2