s1, s2 = input().split()
n = int(input())
A = ['^', '>', 'v', '<']
if n % 2 == 0:
    print("undefined")
elif A[A.index(s2)-1]==s1:
    if n%4==3:
        print('ccw')
    else:
        print('cw')
else:
    if n%4==3:
        print('cw')
    else:
        print('ccw')