a, b, c, d = map(int, input().split(' '))

if (a+b) - (c+d) < 1:
    print(-1)
    quit()


if c == d:
    if ((b-c) < 0 or (a-c-1) < 0):
        print(-1)
        quit()

    if a == c:
        print('74' * d + '7' * (b-a))
        quit()
        
    print('4' * (a-c-1) + '47' * c + '7' * (b - c) + '4')
    quit()
    
if c + 1 == d:
    if (a-c-1 < 0 or b-c-1 < 0):
        print(-1)
        quit()
        
    print('7' + '4' * (a-c-1) + '47' * c + '7' * (b-1-c) + '4')
    quit()
    
if d + 1 == c:
    if a-c < 0 or b-c < 0:
        print(-1)
        quit()
    print('4'*(a-c) + '47' * (c) + '7' * (b-c))
    quit()
    
print(-1)
quit()