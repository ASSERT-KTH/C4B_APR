n, k = map(int, input().split())
time = 240 - k
def solved_problem( t ):
    i, c = 1, 0
    while 1 :
        t = t - 5 * i
        if ((t - 5 * i)<=0):
            break
        c+=1
        i+=1
    return i   
x = solved_problem(time)
if(x>n):
    x=n
print(x)