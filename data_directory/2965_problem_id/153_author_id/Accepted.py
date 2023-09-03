#n = int(input())
#n, m = map(int, input().split())
s = input()
#c = list(map(int, input().split()))
n = int(input())
a = ['v', '<', '^', '>']
k = n % 4
if k % 2 == 0:
    print('undefined')
elif (a.index(s[2]) - a.index(s[0]) ) % 4 == k:
    print('cw')
else:
    print('ccw')