#n = int(input())
#n, m = map(int, input().split()) 
#s = input()
#c = list(map(int, input().split()))
n, m, s = input().split()
n = int(n)
if s == 'month':
    if n == 31:
        print(7)
    elif n == 30:
        print(11)
    else:
        print(12)
else:
    if n == 5 or n == 6:
        print(53)
    else:
        print(52)