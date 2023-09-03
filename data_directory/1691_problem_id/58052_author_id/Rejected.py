import sys
#f = sys.stdin
#f = open("input.txt", "r")
a = [int(i) for i in input().split()]
a.sort()
t = a.count(a[0]) == len(a)
count = sum(a)*2-6
while a[0] > 1:
    a = [i-1 for i in a]
    count += sum(a)*2-6
if t:
    print(count+1)
else:
    print(count)