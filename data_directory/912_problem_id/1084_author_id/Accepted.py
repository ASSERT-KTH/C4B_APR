n, k = map(int, input().split())
time = 240 - k
def solved_problem( t ):
    i = 1
    while 1 :
        if ((t - 5 * i)<0):
            break
        t = t - 5 * i
        i+=1
    return i   
x = solved_problem(time) - 1
if(x>n):
    x=n
print(x)