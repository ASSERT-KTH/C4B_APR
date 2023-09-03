import math

def get_cnt(res):
    n = 1 + math.floor(math.sqrt(2 * res))
    if n * (n-1) / 2 == res:
        return n
    else:
        return -1
        
def calc():
    cnt = list(map(int, input().split()))
    if cnt == [0,0,0,0]:
        return '0'
    #if cnt == [0,1,0,0]:
        #return '01'
    #if cnt == [0,0,1,0]:
        #return '10'
    #if cnt[0] == 0 or cnt[1] == 0 or cnt[2] == 0 or cnt[3] == 0:
        #return "Impossible"

    a = get_cnt(cnt[0])
    b = get_cnt(cnt[3])
    if a == -1 or b == -1 or (a * b) != (cnt[1] + cnt[2]):
        return "Impossible"

    ans = ['0'] * (a + b)
    i = 0
    while b > 0:
        while cnt[1] >= b:
            i = i + 1
            cnt[1] -= b
        b -= 1
        ans[i] = '1'
        i += 1
    return ''.join(ans)
            

print(calc())