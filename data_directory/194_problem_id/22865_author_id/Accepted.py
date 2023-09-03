n = int(input())
m = n
x = 0
mm = n%5
if mm == 0:
    x = m//5
    print(x)
elif m > 5:
    x = m//5
    print(x+1)
elif n<=5:
    print('1')