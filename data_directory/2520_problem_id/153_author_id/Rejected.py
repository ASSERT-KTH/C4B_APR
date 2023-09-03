#n = int(input())
n, m = map(int, input().split())
#s = input() 
#c = list(map(int, input().split()))
x = str(max(n, m))
if x == '1':
    print('5/6')
elif x == '2':
    print('1/3')
elif x == '3':
    print('1/2')
elif x == '4':
    print('2/3')
elif x == '5':
    print('5/6')
else:
    print('1/1')