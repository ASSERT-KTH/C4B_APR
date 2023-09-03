n,k = map(int,input().split())
const = 0
num = 1

while const != -1:
    const += 1
    num = const
    num = k * const
    if num > n:
        print(num)
        break