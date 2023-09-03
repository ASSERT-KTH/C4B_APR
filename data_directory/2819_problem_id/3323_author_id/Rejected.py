import sys
import math

dict = {}
dictMax = {}
value = sys.stdin.readline()
res = str.split(value, ' ')
values = []
first = int(res[0])
second = int(res[1])

def getBiggestDiv(values):
    count2 = 0
    count3 = 0
    for i in values:
        if i%2 == 0:
            count2+=1
        if i%3 == 0:
            count3+=1
    if count2 < 2 and count3 < 2:
        return max(values)
    if count3 >= count2:
        return 3
    else:
        return 2

while first <= second:
    values.append(first)
    first+=1
if len(values) > 4:
    print(2)
    sys.exit(0)

elif len(values) <= 4:
    maxValue = getBiggestDiv(values)
    print(maxValue)
sys.exit(0)
# 1502391711977