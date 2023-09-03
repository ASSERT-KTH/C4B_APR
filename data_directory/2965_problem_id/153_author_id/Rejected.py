#n = int(input())
#n, m = map(int, input().split())
s = input()
#c = list(map(int, input().split()))
n = int(input())
a = ['v', '<', '^', '>']
k = n % 4
if k == 2:
    print('undefined')
elif 4 - a.index(s[2]) + a.index(s[0]) > 0:
    print('cw')
else:
    print('ccw')